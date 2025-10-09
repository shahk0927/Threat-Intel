# AI-Driven Threat Intelligence Automation MVP

## Project Overview

This project develops a Minimum Viable Product (MVP) for an automated AI-powered threat intelligence pipeline tailored for Canadian municipal and law enforcement cybersecurity needs. The system collects, enriches, analyzes, and reports on cyber threats targeting public-sector infrastructure, delivering actionable intelligence to both technical analysts and executive decision-makers.

---

## Core Objective

To build an AI-integrated automated threat intelligence system that identifies, analyzes, and reports on ransomware, phishing, critical infrastructure attacks, and cyber espionage threats relevant to government organizations such as municipalities and law enforcement agencies in Canada.

---

## Project Scope

### In-Scope Activities
- Automated data collection from 3-5 open-source threat intelligence feeds relevant to the Canadian public sector.
- Data enrichment using GeoIP, reputation data, and contextual threat information.
- AI-powered analysis for severity scoring, MITRE ATT&CK framework mapping, and summary generation.
- Web-based dashboard to visualize intelligence with downloadable technical and executive reports.

### Out-of-Scope for MVP
- Live threat mitigation or blocking (no firewall or EDR integrations).
- Full forensic analysis or incident investigation tools.
- Commercial or paid threat intelligence feeds.
- Deep and continuous dark web monitoring (simulated darknet data only).

---

## Essential Threat Types Covered

| Threat Type             | Importance                                           | Example Scenarios                                            |
|------------------------|----------------------------------------------------|-------------------------------------------------------------|
| Ransomware             | Major threat crippling municipal operations         | LockBit, Cl0p targeting city halls, police, and utilities.  |
| Phishing & Spear Phishing | Primary attack vector targeting employees          | Fake emails impersonating government bodies for credential theft. |
| Critical Infrastructure Attacks | Threats to essential services and OT networks      | SCADA system probes, traffic control disruptions.           |
| Cyber Espionage         | State-sponsored intelligence gathering               | APT groups targeting law enforcement and municipal data.    |

---

## Data Sources (Initial MVP)

| Data Source Category      | Specific Feeds/Resources                            | Type of Info Gathered                                       |
|--------------------------|---------------------------------------------------|-------------------------------------------------------------|
| Government & CERT Advisories | Canadian Centre for Cyber Security, CISA KEV Catalog | Alerts, vulnerability info, IOC relevant to public sector.  |
| Public Threat Feeds        | Abuse.ch, AlienVault OTX, Spamhaus                 | Malicious hashes, URLs, IPs, community-vetted indicators.   |
| Darknet & Threat Actor Monitoring | Curated security blogs, simulated darknet datasets     | Threat actor TTPs, leak reports, chatter about government targets. |

---

## Output Formats

### Technical Report (For SOC Analysts)
- Detailed list of IOCs (IPs, domains, hashes).
- Enrichment data (GeoIP, VirusTotal scores, Shodan results).
- MITRE ATT&CK technique mapping.
- AI-generated confidence and severity scores.
- Suggested mitigation recommendations.

### Executive Summary (For Leadership)
- Threat overview and campaign description.
- Business impact focused on municipal services.
- Key affected assets and departments.
- Strategic recommendations for leadership action.
- Visual representation of threat severity trends.

---

## Tools & Technologies
- Python (requests, pandas, BeautifulSoup, NLP libraries like HuggingFace Transformers).
- Threat intelligence APIs (VirusTotal, Abuse.ch, AlienVault OTX).
- MITRE ATT&CK mapping using official ATT&CK data.
- Dashboard & report visualization with Streamlit or Dash.
- PDF report generation tools.

---

## Getting Started

1. Clone this repository.
2. Install dependencies listed in `requirements.txt`.
3. Configure API keys for data sources (free tier or public APIs).
4. Run data collection and enrichment scripts.
5. Launch dashboard or generate reports.
6. Review and interpret findings.

---

## Future Work & Enhancements
- Integration of live dark web monitoring.
- Automated alerting and SOC workflow integration.
- Advanced AI models for anomaly detection and threat prediction.
- Expanded coverage for additional public sector threat vectors.

---

## License

This project is open-source and available under the MIT License.

---

## Contact

For questions or collaborations, please contact [Your Name] at [Your Email].

