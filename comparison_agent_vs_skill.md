# Comparison: Field-Data-Analyst Agent vs Pattern-Researcher Skill

## Overview

Both approaches produced OT data ingestion pattern reports from the same Salesforce UCO dataset (650 active U4/U5 use cases). This document compares their methodologies, outputs, and use cases.

---

## Side-by-Side Comparison

| Aspect | Field-Data-Analyst Agent | Pattern-Researcher Skill |
|--------|--------------------------|--------------------------|
| **Type** | Orchestrator Agent (dynamic) | Composite Skill (prescriptive) |
| **Model** | Claude Opus (reasoning) | User's session model (Sonnet) |
| **Workflow** | Inferred from query | Explicit step-by-step instructions |
| **Output Style** | Analytical insights + data | Structured template + data |
| **Tone** | Consulting analyst | SA reference documentation |
| **Target Audience** | Internal stakeholders (AE, SA, Product) | Solutions Architects |
| **Reusability** | General-purpose (any data query) | Pattern-specific (OT, GenAI, etc.) |
| **Documentation** | Agent instructions in .md file | Skill instructions + resources |
| **Invocation** | `/field-data-analyst` + question | `/pattern-researcher` + pattern definition |

---

## Content Differences

### 1. Report Structure

**Field-Data-Analyst (Agent):**
```
├── Executive Summary (insights-first)
├── Key Findings (bullet points)
├── Customer Evidence (narrative style)
├── Industry Distribution Analysis
├── Architecture Patterns Observed
├── Recommendations for Pattern Positioning
├── Data Quality Notes
└── Summary: What the Data Tells Us
```

**Pattern-Researcher (Skill):**
```
├── 01 — Scope and Pattern Definition
├── 02 — Customer Evidence: Closest Matches
├── 03 — Analogous Patterns
├── 04 — Industry Distribution
├── 05 — Reference Architecture Patterns
├── 06 — Key Takeaways
├── 07 — Recommendations (Sales, SA, Product)
├── 08 — Data Sources
├── 09 — Data Quality Notes
└── Appendix A: Full Customer List
```

**Key Difference:** Agent uses **narrative flow**, Skill uses **numbered sections** (SA reference style)

---

### 2. Analytical Depth

**Field-Data-Analyst (Agent) - Deeper Insights:**
- ✅ **Pattern Gap Analysis:** "Only 2 customers explicitly mention AWS Greengrass/SiteWise, suggesting either underreporting or technology substitution"
- ✅ **Critical Insight Section:** Dedicated section for "what the data tells us"
- ✅ **Competitive Intelligence:** "Zerobus appears 3 times as Kafka replacement - competitive win story"
- ✅ **Root Cause Analysis:** "UCO naming inconsistency" vs "customers actually using these technologies"
- ✅ **Strategic Recommendations:** "Broaden 'Greengrass/SiteWise' narrative to edge-agnostic lakehouse"

**Pattern-Researcher (Skill) - Structured Coverage:**
- ✅ **Tier Classification:** Explicit Tier 1/2/3 categorization (80%/50%/30% match thresholds)
- ✅ **Comprehensive Tables:** Customer evidence in scannable table format
- ✅ **Pattern Diagrams:** 4 reference architectures (A, B, C, D) with ASCII diagrams
- ✅ **Actionable Recommendations:** Separated by role (Sales, SA, Product)
- ✅ **Data Quality Section:** Explicit limitations and follow-up actions

---

### 3. Customer Evidence Presentation

**Field-Data-Analyst (Agent):**
```markdown
### Pattern A: AVEVA Connect → Databricks

#### **Alinta Servco Pty Ltd** 🟢 U5 - Onboarding
- **UCO:** Aveva Connect - OT Data Ingest
- **Status:** Active (Target: May 2026)
- **DSA:** Chuong Vu
- **Industry:** Energy/Utilities
- **Pattern:** AVEVA Connect (OT edge) → Databricks
- **Significance:** AVEVA is OSIsoft's successor platform...

**Analysis:** AVEVA Connect is functionally equivalent to AWS SiteWise...
```

**Pattern-Researcher (Skill):**
```markdown
#### **Alinta Servco Pty Ltd** | Energy/Utilities | U5 | Active

- **Pattern:** AVEVA Connect → Databricks OT Data Ingest
- **Description:** Alinta is deploying AVEVA Connect to ingest OT data from energy assets...
- **Stage:** U5 (Onboarding) | **Monthly:** TBD | **DSA:** Chuong Vu
- **Target Date:** May 2026
```

**Key Difference:**
- Agent: **Narrative + inline analysis**
- Skill: **Structured cards + consistent formatting**

---

### 4. Recommendations Section

**Field-Data-Analyst (Agent) - Strategic:**
```markdown
### 1. Broaden "Greengrass/SiteWise" Narrative

**Current Search:** AWS Greengrass, AWS SiteWise
**Reality:** Customers use AVEVA, PI Historian, custom MQTT, Zerobus

**Recommendation:** Position Databricks as edge-agnostic lakehouse

### 2. Highlight Zerobus for Kafka Replacement

3 active U5 UCOs show Kafka → Zerobus migration. This is a competitive win story.

**Action:** Create SA reference architecture comparing Kafka vs Zerobus paths.
```

**Pattern-Researcher (Skill) - Role-Specific:**
```markdown
### For Sales (AE/SAE)

**Target Industries:**
- Manufacturing, Energy & Utilities, Transportation

**Competitive Positioning:**
- vs AWS IoT Analytics: "Vendor-agnostic edge support"
- vs Kafka-heavy stacks: "Zerobus eliminates ops overhead"

**Reference Customers:**
- Manufacturing IoT: General Motors
- Energy OT: NRG Energy

### For Solutions Architects (SA/DSA)

**Architecture Pattern Priority:**
1. Pattern C (Zerobus) - New deployments
2. Pattern B (Kafka) - Existing infrastructure
...

**Partner Ecosystem Engagement:**
- AVEVA (OSIsoft), AWS IoT, Confluent, Rockwell Automation

**Technical Deep Dives Needed:**
- Autoloader performance tuning for sub-second sensors
- Time-series optimization in Delta Lake
...
```

**Key Difference:**
- Agent: **Strategic positioning** (why and what)
- Skill: **Tactical execution** (who, when, how)

---

### 5. Data Quality & Limitations

**Field-Data-Analyst (Agent):**
```markdown
### Limitations of This Analysis

1. **UCO Naming Inconsistency:** Some customers may use Greengrass/SiteWise but don't mention it
2. **Implementation Notes Not Analyzed:** Deeper patterns require reading description fields
3. **Consumption Data Missing:** No monthly $ (requires Logfood join)
4. **Stage Validation Needed:** U4/U5 should be validated against consumption

### Next Steps for Complete Analysis

1. Deep Dive on Top 20
2. Logfood Join
3. SA Interviews
4. UCO Hygiene Updates
```

**Pattern-Researcher (Skill):**
```markdown
## 09 — Data Quality Notes

### Limitations

1. **UCO Naming Inconsistency:** [Same as agent]
2. **Description Fields Not Analyzed:** [Same as agent]
3. **Consumption Validation Missing:** [Same as agent]
4. **AVEVA ≈ SiteWise Equivalence Assumption:** Treating as equivalent based on functional similarity

### Recommended Follow-Up Actions

1. Deep Dive Top 20: Read full descriptions
2. DSA Interviews: Contact Chuong Vu, Archana, Van Vaidya
3. Logfood Access: Resolve IP ACL
4. UCO Hygiene: Update names with tech stack
5. Partner Validation: Confirm AVEVA architecture with partnership team
```

**Key Difference:**
- Agent: **Contextual notes** (what's missing)
- Skill: **Explicit limitations + follow-up checklist** (standardized format)

---

## Strengths & Weaknesses

### Field-Data-Analyst Agent

**Strengths:**
- ✅ Deeper analytical insights (pattern gaps, strategic recommendations)
- ✅ Critical thinking about data quality (what it means, not just what's missing)
- ✅ Narrative flow easier to read for executives
- ✅ Flexible approach (adapts to any data analysis question)
- ✅ Powered by Opus (stronger reasoning for complex analysis)

**Weaknesses:**
- ❌ Less consistent formatting (varies by analyst/question)
- ❌ Not repeatable (different prompts → different structures)
- ❌ Harder to share methodology (lives in agent's reasoning, not documented)
- ❌ No template (SA needs to interpret and adapt for their use)

---

### Pattern-Researcher Skill

**Strengths:**
- ✅ Highly consistent structure (numbered sections, table formats)
- ✅ Repeatable methodology (anyone can follow the steps)
- ✅ Role-specific recommendations (Sales, SA, Product)
- ✅ SA reference format (ready to share with customers/partners)
- ✅ Template-driven (easy to apply to other patterns: GenAI, Streaming, Delta Sharing)
- ✅ Documented instructions (skill file captures the process)

**Weaknesses:**
- ❌ More rigid format (less narrative flexibility)
- ❌ Potentially more verbose (all sections required even if sparse)
- ❌ Less analytical depth (focuses on structure over insights)
- ❌ Requires manual pattern definition (keywords, tiers, etc.)

---

## When to Use Each

### Use Field-Data-Analyst Agent When:

1. **Exploratory Analysis:** You're investigating a question and don't know the answer structure yet
2. **Executive Presentation:** Need insights and strategic recommendations for leadership
3. **Ad-Hoc Queries:** One-off analysis that won't be repeated
4. **Complex Reasoning:** Need Opus-level analytical thinking (e.g., "Why is this pattern rare?")
5. **Multi-Faceted Questions:** Combining UCO + consumption + org hierarchy data

**Example Prompts:**
- "Why do so few customers use Greengrass despite AWS partnership?"
- "Analyze consumption trends for my top 10 accounts and identify churn risk"
- "What patterns separate our fastest-growing vs stagnant enterprise customers?"

---

### Use Pattern-Researcher Skill When:

1. **Repeatable Research:** You'll run this analysis monthly/quarterly for different patterns
2. **SA Reference Material:** Creating documentation for SA team or partners
3. **Competitive Intelligence:** Building standardized competitive analysis reports
4. **Pattern Library Building:** Creating a portfolio of pattern analyses (OT, GenAI, Streaming, etc.)
5. **Consistent Reporting:** Need same format across multiple analysts/regions

**Example Patterns:**
- OT Data Ingestion (this report)
- GenAI Production Deployments
- Delta Sharing & Data Marketplace Adoption
- Lakehouse Monitoring & Drift Detection
- UC Migration Patterns
- Serverless Adoption Analysis

---

## Hybrid Approach (Recommended)

**Best Practice:** Use both in sequence

### Step 1: Agent for Discovery
```bash
/field-data-analyst

"Analyze OT data ingestion patterns - are customers using AWS Greengrass/SiteWise,
or are they using alternative edge platforms? What's the competitive landscape?"
```

**Output:** Deep insights, strategic recommendations, pattern gaps identified

### Step 2: Skill for Documentation
```bash
/pattern-researcher

Pattern: OT Data Ingestion via AWS IoT Services
Keywords: [from agent insights]
Output: SA Reference Report (structured format)
```

**Output:** Consistent, shareable, repeatable documentation

### Combined Workflow

1. **Agent** identifies: "Only 2 customers use AWS IoT services explicitly, but 21 use Kafka/streaming"
2. **Agent** recommends: "Broaden narrative to edge-agnostic, highlight Zerobus vs Kafka"
3. **Skill** documents: Tier 1 (AVEVA), Tier 2 (Kafka), Tier 3 (General IoT) with reference architectures
4. **Skill** produces: SA-ready report with role-specific recommendations

---

## Example: Combining Both Approaches

### Agent Output (Insight):
> "Pattern Gap Identified: No customer runs the complete Greengrass → Kafka → S3 → Autoloader chain.
> Customers prefer simpler paths: Greengrass → S3 → Autoloader (skip Kafka) OR Kafka → Autoloader (skip Greengrass)."

### Skill Captures This in Pattern Library:
```markdown
## Pattern A: Edge → Lakehouse (No Streaming Layer)
OT Sensors → AVEVA/Greengrass → S3 → Autoloader → Delta Lake
Customers: Alinta, TASA

## Pattern B: Streaming → Lakehouse (No Edge Layer)
App/IoT Sources → Kafka → S3 → Autoloader → Delta Lake
Customers: NRG, DraftKings, Flipp

## Pattern C: Databricks-Native (Simplified)
IoT Sources → Zerobus → Delta Lake
Customers: Casey's, PAR Tech, Quartile
```

**Result:** Agent's insight becomes skill's documented pattern library.

---

## File Locations

**Agent-Style Report:**
- `/Users/pravin.varma/Documents/Demo/math-learning/report_field_data_analyst.md`

**Skill-Style Report:**
- `/Users/pravin.varma/Documents/Demo/math-learning/report_pattern_researcher.md`

**Skill Definition:**
- `/Users/pravin.varma/.vibe/marketplace/plugins/fe-internal-tools/skills/pattern-researcher/SKILL.md`

---

## Recommendation for Your Use Case

**Create the pattern-researcher skill** for the following reasons:

1. ✅ **Repeatability:** You'll likely run OT, GenAI, streaming, and other pattern analyses regularly
2. ✅ **Team Sharing:** Other SAs can use the same methodology
3. ✅ **Consistency:** Standardized format for SA reference library
4. ✅ **Documentation:** Captures the process, not just the output
5. ✅ **Scalability:** Easy to expand to new patterns (just add keywords + run)

**Use the agent for:**
- Initial exploration ("What patterns exist?")
- Strategic questions ("Why are customers avoiding X technology?")
- Executive synthesis ("What are the top 3 insights for leadership?")

---

**Conclusion:** The skill provides structure and repeatability, while the agent provides depth and flexibility. Use the agent to discover insights, then use the skill to document and share them in a consistent format.
