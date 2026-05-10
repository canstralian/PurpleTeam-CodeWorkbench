# app.py
# Authorized Security Assessment Workflow
# Run: streamlit run app.py

from __future__ import annotations

import socket
import ssl
from datetime import datetime, timezone
from urllib.parse import urlparse, urljoin

import httpx
import streamlit as st
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field, HttpUrl


class Scope(BaseModel):
    target_url: HttpUrl
    authorization_confirmed: bool
    engagement_notes: str = ""


class Finding(BaseModel):
    title: str
    severity: str
    evidence: str
    recommendation: str


SECURITY_HEADERS = [
    "strict-transport-security",
    "content-security-policy",
    "x-frame-options",
    "x-content-type-options",
    "referrer-policy",
    "permissions-policy",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def fetch_url(url: str) -> dict:
    try:
        with httpx.Client(timeout=10, follow_redirects=True) as client:
            response = client.get(url)
        return {
            "ok": True,
            "status_code": response.status_code,
            "final_url": str(response.url),
            "headers": dict(response.headers),
            "text": response.text[:200_000],
        }
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def check_security_headers(headers: dict) -> list[dict]:
    normalized = {k.lower(): v for k, v in headers.items()}
    results = []

    for header in SECURITY_HEADERS:
        present = header in normalized
        results.append(
            {
                "control": header,
                "status": "present" if present else "missing",
                "value": normalized.get(header, ""),
            }
        )

    return results


def get_tls_info(url: str) -> dict:
    parsed = urlparse(url)
    hostname = parsed.hostname

    if not hostname:
        return {"ok": False, "error": "Invalid hostname"}

    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=8) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        return {
            "ok": True,
            "subject": cert.get("subject"),
            "issuer": cert.get("issuer"),
            "not_before": cert.get("notBefore"),
            "not_after": cert.get("notAfter"),
        }
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def extract_links(base_url: str, html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)

        if parsed.scheme in {"http", "https"}:
            links.add(absolute.split("#")[0])

    return sorted(links)


def build_markdown_report(scope: Scope, recon: dict, findings: list[Finding]) -> str:
    lines = [
        "# Authorized Security Assessment Report",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Scope",
        "",
        f"- Target: `{scope.target_url}`",
        f"- Authorization confirmed: `{scope.authorization_confirmed}`",
        f"- Notes: {scope.engagement_notes or 'None provided'}",
        "",
        "## Passive Recon Summary",
        "",
        f"- HTTP status: `{recon.get('status_code', 'n/a')}`",
        f"- Final URL: `{recon.get('final_url', 'n/a')}`",
        "",
        "## Security Header Review",
        "",
    ]

    for item in recon.get("security_headers", []):
        lines.append(f"- `{item['control']}`: **{item['status']}**")

    lines.extend(["", "## TLS Review", ""])

    tls = recon.get("tls", {})
    if tls.get("ok"):
        lines.append(f"- Certificate valid from: `{tls.get('not_before')}`")
        lines.append(f"- Certificate valid until: `{tls.get('not_after')}`")
    else:
        lines.append(f"- TLS check error: `{tls.get('error', 'unknown')}`")

    lines.extend(["", "## Findings", ""])

    if not findings:
        lines.append("No findings recorded.")
    else:
        for idx, finding in enumerate(findings, start=1):
            lines.extend(
                [
                    f"### {idx}. {finding.title}",
                    "",
                    f"Severity: **{finding.severity}**",
                    "",
                    "**Evidence**",
                    "",
                    finding.evidence,
                    "",
                    "**Recommendation**",
                    "",
                    finding.recommendation,
                    "",
                ]
            )

    return "\n".join(lines)


st.set_page_config(
    page_title="Authorized Security Assessment Workflow",
    page_icon="🛡️",
    layout="wide",
)

st.title("Authorized Security Assessment Workflow")
st.caption("Scope-gated passive recon, evidence logging, and report generation.")

if "findings" not in st.session_state:
    st.session_state.findings = []

with st.sidebar:
    st.header("Scope Gate")

    target_url = st.text_input("Target URL", placeholder="https://example.com")
    authorization_confirmed = st.checkbox(
        "I confirm I am authorized to assess this target"
    )
    engagement_notes = st.text_area(
        "Engagement notes",
        placeholder="Bug bounty program, internal asset, written permission, etc.",
    )

    run_recon = st.button("Run Passive Assessment")

if not target_url:
    st.warning("Enter an authorized target URL to begin. Humanity survives another second.")
    st.stop()

try:
    scope = Scope(
        target_url=target_url,
        authorization_confirmed=authorization_confirmed,
        engagement_notes=engagement_notes,
    )
except Exception as exc:
    st.error(f"Invalid scope input: {exc}")
    st.stop()

if not scope.authorization_confirmed:
    st.error("Authorization is required before running any assessment.")
    st.stop()

tab_recon, tab_findings, tab_report = st.tabs(
    ["Passive Recon", "Findings", "Report"]
)

recon_data = st.session_state.get("recon_data")

if run_recon:
    response = fetch_url(str(scope.target_url))

    if not response["ok"]:
        st.error(response["error"])
        st.stop()

    headers_review = check_security_headers(response["headers"])
    tls_info = get_tls_info(str(scope.target_url))
    links = extract_links(response["final_url"], response["text"])

    recon_data = {
        **response,
        "security_headers": headers_review,
        "tls": tls_info,
        "links": links[:100],
        "checked_at": utc_now(),
    }

    st.session_state.recon_data = recon_data

with tab_recon:
    if not recon_data:
        st.info("Run the passive assessment from the sidebar.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("HTTP")
            st.write("Status:", recon_data["status_code"])
            st.write("Final URL:", recon_data["final_url"])
            st.write("Checked:", recon_data["checked_at"])

        with col2:
            st.subheader("TLS")
            st.json(recon_data["tls"])

        st.subheader("Security Headers")
        st.dataframe(recon_data["security_headers"], use_container_width=True)

        st.subheader("Discovered Links")
        st.dataframe(recon_data["links"], use_container_width=True)

with tab_findings:
    st.subheader("Add Finding")

    title = st.text_input("Finding title")
    severity = st.selectbox(
        "Severity",
        ["Informational", "Low", "Medium", "High", "Critical"],
    )
    evidence = st.text_area("Evidence")
    recommendation = st.text_area("Recommendation")

    if st.button("Save Finding"):
        if not title or not evidence or not recommendation:
            st.error("Title, evidence, and recommendation are required.")
        else:
            st.session_state.findings.append(
                Finding(
                    title=title,
                    severity=severity,
                    evidence=evidence,
                    recommendation=recommendation,
                )
            )
            st.success("Finding saved.")

    st.subheader("Current Findings")

    if not st.session_state.findings:
        st.info("No findings recorded.")
    else:
        for idx, finding in enumerate(st.session_state.findings, start=1):
            with st.expander(f"{idx}. {finding.title} [{finding.severity}]"):
                st.write(finding.evidence)
                st.write("Recommendation:")
                st.write(finding.recommendation)

with tab_report:
    if not recon_data:
        st.info("Run recon before generating a report.")
    else:
        report = build_markdown_report(
            scope=scope,
            recon=recon_data,
            findings=st.session_state.findings,
        )

        st.subheader("Markdown Report")
        st.text_area("Report", report, height=500)

        st.download_button(
            "Download Report",
            data=report,
            file_name="authorized_security_assessment_report.md",
            mime="text/markdown",
        )