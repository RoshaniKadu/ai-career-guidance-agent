import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Guidance Platform",
    page_icon="🚀",
    layout="wide"
)

# ---------------- JOB DATA ----------------
JOB_DATA = {
    "Data Analyst": {
        "skills": ["python", "sql", "excel", "power bi", "statistics"],
        "salary": {
            "Fresher": "₹4 – 6 LPA",
            "2-3 Years": "₹8 – 12 LPA",
            "10+ Years": "₹25+ LPA"
        }
    },
    "Cloud Engineer": {
        "skills": ["aws", "linux", "docker", "networking"],
        "salary": {
            "Fresher": "₹5 – 7 LPA",
            "2-3 Years": "₹10 – 15 LPA",
            "10+ Years": "₹30+ LPA"
        }
    },
    "Software Developer": {
        "skills": ["python", "java", "git", "problem solving"],
        "salary": {
            "Fresher": "₹4 – 6 LPA",
            "2-3 Years": "₹8 – 14 LPA",
            "10+ Years": "₹28+ LPA"
        }
    },
    "ML Engineer": {
        "skills": ["python", "machine learning", "data science"],
        "salary": {
            "Fresher": "₹6 – 8 LPA",
            "2-3 Years": "₹12 – 18 LPA",
            "10+ Years": "₹35+ LPA"
        }
    }
}

# ---------------- LOGIC ----------------
def analyze_profile(skills, experience):
    skills = [s.strip().lower() for s in skills.split(",") if s.strip()]
    results = []

    score = min(100, len(skills) * 12 + experience * 6)

    if score >= 75:
        readiness = "Job Ready ✅"
    elif score >= 45:
        readiness = "Partially Job Ready ⚠️"
    else:
        readiness = "Needs Skill Development ❌"

    for role, data in JOB_DATA.items():
        matched = set(skills) & set(data["skills"])
        missing = set(data["skills"]) - set(skills)

        if len(matched) >= 2:
            results.append({
                "role": role,
                "matched": list(matched),
                "missing": list(missing),
                "salary": data["salary"]
            })

    return score, readiness, results

# ---------------- UI ----------------
st.title("🚀 AI-Powered Career Guidance Platform")
st.markdown("### Smart Resume & Skill Analysis with Salary Insights")

st.divider()

# -------- INPUT SECTION --------
col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("👤 Candidate Name")

with col2:
    education = st.selectbox(
        "🎓 Highest Qualification",
        ["Diploma", "Graduate", "Post Graduate", "Other"]
    )

with col3:
    experience = st.number_input(
        "💼 Years of Experience",
        min_value=0,
        max_value=20,
        step=1
    )

skills = st.text_area(
    "🛠️ Enter Your Skills (comma separated)",
    placeholder="Python, SQL, AWS"
)

st.divider()

# -------- BUTTONS --------
colA, colB = st.columns(2)

with colA:
    analyze_btn = st.button("🔍 Analyze Career Profile")

with colB:
    demo_btn = st.button("🎯 Load Demo Profile")

if demo_btn:
    skills = "Python, SQL, AWS"
    experience = 1

# -------- OUTPUT --------
if analyze_btn and skills:

    score, readiness, results = analyze_profile(skills, experience)

    st.subheader("📊 Profile Summary")

    colX, colY, colZ = st.columns(3)
    colX.metric("Employability Score", f"{score}%")
    colY.metric("Readiness Status", readiness)
    colZ.metric("Experience", f"{experience} Years")

    st.divider()

    if results:
        st.subheader("🎯 Recommended Career Paths")

        for r in results:
            with st.container():
                st.markdown(f"## 💼 {r['role']}")

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.markdown("### ✅ Matched Skills")
                    for s in r["matched"]:
                        st.success(s.title())

                with c2:
                    st.markdown("### ❌ Missing Skills")
                    if r["missing"]:
                        for m in r["missing"]:
                            st.warning(m.title())
                    else:
                        st.success("No skill gap 🎉")

                with c3:
                    st.markdown("### 💰 Salary Insights")
                    st.write("👶 Fresher:", r["salary"]["Fresher"])
                    st.write("👨‍💻 2–3 Years:", r["salary"]["2-3 Years"])
                    st.write("🧓 10+ Years:", r["salary"]["10+ Years"])

                st.divider()

    else:
        st.warning("⚠️ No suitable role found. Improve skills to unlock opportunities.")

    st.subheader("📌 Final AI Recommendation")
    st.info(
        f"{name if name else 'Candidate'}, focus on improving missing skills to increase salary potential and job readiness."
    )

else:
    st.info("👆 Enter details and click **Analyze Career Profile**")
