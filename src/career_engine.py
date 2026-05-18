class BaseCareer:

    def __init__(self, name, skill_graph, meta):
        self.name = name
        self.skill_graph = skill_graph
        self.meta = meta
    def generate(self, user_skills):
        user_skills_lower = [s.strip().lower() for s in user_skills]

        roadmap = []
        next_skill = None
        next_skill_details = None

        for skill, details in self.skill_graph.items():

            completed = skill.lower() in user_skills_lower

            if not completed and next_skill is None:
                next_skill = skill
                next_skill_details = details

            roadmap.append({
                "skill": skill,
                "completed": completed,
                "time": details.get("time"),
                "resources": details.get("resources", []),
                "projects": details.get("projects", []),
                "next": details.get("next")
            })

        total = len(self.skill_graph)
        completed_count = sum(1 for r in roadmap if r["completed"])
        progress = round((completed_count / total) * 100, 2)

        missing_skills = [r["skill"] for r in roadmap if not r["completed"]]

        # SAFE fallback
        if next_skill_details:
            next_time = next_skill_details.get("time")
            next_projects = next_skill_details.get("projects", [])
            next_resources = next_skill_details.get("resources", [])
        else:
            next_time = None
            next_projects = []
            next_resources = []

        return {
            "career": self.name,
            "roadmap": roadmap,
            "progress": progress,
            "completed_count": completed_count,
            "total_skills": total,
            "progress_label": (
                "Beginner" if progress < 30
                else "Intermediate" if progress < 70
                else "Advanced"
            ),
            "missing_skills": missing_skills,
            "next_skill": next_skill,
            "next_time": next_time,
            "next_projects": next_projects,
            "next_resources": next_resources,
            "roles": self.meta["roles"],
            "resources": self.meta["resources"],
            "time": self.meta["time"],
            "demand": self.meta["demand"],
            "salary": self.meta["salary"]
        }

        # # Skill Dependency Intelligence
        # next_skill = None
        # next_skill_details = None

        # for skill in self.skill_graph:
        #     if skill.lower() not in user_skills_lower:
        #         next_skill = skill
        #         next_skill_details = self.skill_graph[skill]
        #         break

        # return {
        #     "career": self.name,
        #     "roadmap": roadmap,
        #     "progress": progress,
        #     "missing_skills": missing_skills,
        #     "next_skill": next_skill,
        #     "next_time": next_skill_details["time"] if next_skill else None,
        #     "next_projects": next_skill_details["projects"] if next_skill else [],
        #     "next_resources": next_skill_details["resources"] if next_skill else [],
        #     "roles": self.meta["roles"],
        #     "resources": self.meta["resources"],
        #     "time": self.meta["time"],
        #     "demand": self.meta["demand"],
        #     "salary": self.meta["salary"]
        # }


# ---------------- FRONTEND CAREER ----------------

frontend_graph = {
    "HTML": {
        "next": "CSS",
        "time": "2 weeks",
        "resources": ["MDN HTML", "YouTube HTML"],
        "projects": ["Resume Page", "Basic Portfolio"]
    },
    "CSS": {
        "next": "JavaScript",
        "time": "3 weeks",
        "resources": ["MDN CSS", "freeCodeCamp"],
        "projects": ["Landing Page", "Business Website"]
    },
    "JavaScript": {
        "next": "React",
        "time": "4 weeks",
        "resources": ["Eloquent JS", "YouTube JS"],
        "projects": ["Todo App", "Weather App"]
    },
    "React": {
        "next": "Node.js",
        "time": "4 weeks",
        "resources": ["React Docs"],
        "projects": ["React Portfolio"]
    },
    "Node.js": {
        "next": "MongoDB",
        "time": "3 weeks",
        "resources": ["Node Docs"],
        "projects": ["REST API"]
    },
    "MongoDB": {
        "next": None,
        "time": "2 weeks",
        "resources": ["Mongo Docs"],
        "projects": ["Full Stack CRUD"]
    }
}

frontend_meta = {
    "roles": ["Frontend Developer", "React Developer"],
    "resources": ["freeCodeCamp", "MDN", "YouTube"],
    "time": "5-7 months",
    "demand": "High",
    "salary": "4 - 15 LPA"
}

frontend_career = BaseCareer(
    "Frontend Developer",
    frontend_graph,
    frontend_meta
)


# ---------------- AI/ML CAREER ----------------

ai_graph = {
    "Python": {
        "next": "Machine Learning",
        "time": "4 weeks",
        "resources": ["YouTube Python", "Coursera"],
        "projects": ["Basic ML Model"]
    },
    "Machine Learning": {
        "next": "Deep Learning",
        "time": "6 weeks",
        "resources": ["Andrew Ng Course"],
        "projects": ["Regression Model"]
    },
     "Deep Learning": {
        "next": "TensorFlow",
        "time": "5 weeks",
        "resources": ["YouTube DL"],
        "projects": ["Image Classifier"]
    },
    "TensorFlow": {
        "next": "MLOps",
        "time": "4 weeks",
        "resources": ["Docs"],
        "projects": ["DL Model"]
    },
    "MLOps": {
        "next": None,
        "time": "3 weeks",
        "resources": ["YouTube"],
        "projects": ["Model Deployment"]
    }
}


ai_meta = {
    "roles": ["ML Engineer", "AI Engineer"],
    "resources": ["Coursera", "Kaggle"],
    "time": "8-12 months",
    "demand": "Very High",
    "salary": "8 - 25 LPA"
}

ai_career = BaseCareer(
    "AI/ML Engineer",
    ai_graph,
    ai_meta
)

# ---------------- CLOUD CAREER ----------------

cloud_graph = {
    "Linux": {
        "next": "Networking",
        "time": "2 weeks",
        "resources": ["YouTube Linux"],
        "projects": ["Linux Setup"]
    },
    "Networking": {
        "next": "AWS",
        "time": "3 weeks",
        "resources": ["Networking Docs"],
        "projects": ["Network Lab"]
    },
    "AWS": {
        "next": "Docker",
        "time": "4 weeks",
        "resources": ["AWS Docs"],
        "projects": ["Deploy App"]
    },
    "Docker": {
        "next": "Kubernetes",
        "time": "3 weeks",
        "resources": ["Docker Docs"],
        "projects": ["Container App"]
    },
    "Kubernetes": {
        "next": None,
        "time": "4 weeks",
        "resources": ["K8s Docs"],
        "projects": ["Cluster Setup"]
    }
}

cloud_meta = {
    "roles": ["Cloud Engineer"],
    "resources": ["AWS"],
    "time": "6-10 months",
    "demand": "Very High",
    "salary": "8 - 30 LPA"
}

cloud_career = BaseCareer(
    "Cloud Engineer",
    cloud_graph,
    cloud_meta
)


# ---------------- DEVOPS CAREER ----------------

devops_graph = {
    "Linux": {
        "next": "Git",
        "time": "2 weeks",
        "resources": ["Linux Docs"],
        "projects": ["Linux Practice"]
    },
    "Git": {
        "next": "Docker",
        "time": "2 weeks",
        "resources": ["Git Docs"],
        "projects": ["Version Control"]
    },
    "Docker": {
        "next": "CI/CD",
        "time": "3 weeks",
        "resources": ["Docker Docs"],
        "projects": ["Containers"]
    },
    "CI/CD": {
        "next": "Kubernetes",
        "time": "3 weeks",
        "resources": ["Jenkins"],
        "projects": ["Pipeline"]
    },
    "Kubernetes": {
        "next": None,
        "time": "4 weeks",
        "resources": ["K8s Docs"],
        "projects": ["Cluster"]
    }
}

devops_meta = {
    "roles": ["DevOps Engineer"],
    "resources": ["YouTube"],
    "time": "8-12 months",
    "demand": "Very High",
    "salary": "8 - 25 LPA"
}

devops_career = BaseCareer(
    "DevOps Engineer",
    devops_graph,
    devops_meta
)

# ---------------- CYBERSECURITY CAREER ----------------

cyber_graph = {
    "Networking": {
        "next": "Linux",
        "time": "3 weeks",
        "resources": ["Networking Basics"],
        "projects": ["Network Lab"]
    },
    "Linux": {
        "next": "Security Tools",
        "time": "3 weeks",
        "resources": ["Linux Docs"],
        "projects": ["Linux Practice"]
    },
    "Security Tools": {
        "next": "Ethical Hacking",
        "time": "4 weeks",
        "resources": ["TryHackMe"],
        "projects": ["Scan System"]
    },
    "Ethical Hacking": {
        "next": "Pen Testing",
        "time": "4 weeks",
        "resources": ["HTB"],
        "projects": ["Hack Lab"]
    },
    "Pen Testing": {
        "next": None,
        "time": "4 weeks",
        "resources": ["Docs"],
        "projects": ["Pentest"]
    }
}

cyber_meta = {
    "roles": ["Security Analyst"],
    "resources": ["TryHackMe"],
    "time": "6-10 months",
    "demand": "High",
    "salary": "6 - 20 LPA"
}

cyber_career = BaseCareer(
    "Cybersecurity Analyst",
    cyber_graph,
    cyber_meta
)

# ---------------- POWER BI CAREER ----------------

powerbi_graph = {
    "Excel": {
        "next": "SQL",
        "time": "2 weeks",
        "resources": ["Excel Tutorials"],
        "projects": ["Data Sheets"]
    },
    "SQL": {
        "next": "Power BI",
        "time": "3 weeks",
        "resources": ["SQL Docs"],
        "projects": ["Query Analysis"]
    },
    "Power BI": {
        "next": "DAX",
        "time": "4 weeks",
        "resources": ["Power BI Docs"],
        "projects": ["Dashboard"]
    },
    "DAX": {
        "next": "Data Modeling",
        "time": "3 weeks",
        "resources": ["Docs"],
        "projects": ["KPI Metrics"]
    },
    "Data Modeling": {
        "next": None,
        "time": "3 weeks",
        "resources": ["Docs"],
        "projects": ["Model Design"]
    }
}

powerbi_meta = {
    "roles": ["BI Developer"],
    "resources": ["Microsoft"],
    "time": "3-5 months",
    "demand": "High",
    "salary": "5 - 15 LPA"
}

powerbi_career = BaseCareer(
    "Power BI Expert",
    powerbi_graph,
    powerbi_meta
)

# ---------------- PRODUCT MANAGER CAREER ----------------

product_graph = {
    "Product Thinking": {
        "next": "Market Research",
        "time": "2 weeks",
        "resources": ["YouTube"],
        "projects": ["Case Study"]
    },
    "Market Research": {
        "next": "Agile",
        "time": "2 weeks",
        "resources": ["Docs"],
        "projects": ["Survey Analysis"]
    },
    "Agile": {
        "next": "SQL Basics",
        "time": "3 weeks",
        "resources": ["Scrum"],
        "projects": ["Sprint Plan"]
    },
    "SQL Basics": {
        "next": "Analytics",
        "time": "2 weeks",
        "resources": ["SQL Docs"],
        "projects": ["Query Analysis"]
    },
    "Analytics": {
        "next": None,
        "time": "3 weeks",
        "resources": ["YouTube"],
        "projects": ["Metrics Dashboard"]
    }
}

product_meta = {
    "roles": ["Product Manager"],
    "resources": ["Coursera"],
    "time": "6-9 months",
    "demand": "High",
    "salary": "10 - 35 LPA"
}

product_career = BaseCareer(
    "Product Manager",
    product_graph,
    product_meta
)

# ---------------- DATA ANALYST CAREER ----------------

data_analyst_graph = {
    "Python": {
        "next": "Pandas",
        "time": "3 weeks",
        "resources": ["YouTube Python", "freeCodeCamp"],
        "projects": ["Data Cleaning Project"]
    },
    "Pandas": {
        "next": "SQL",
        "time": "3 weeks",
        "resources": ["Pandas Docs", "Kaggle"],
        "projects": ["Data Analysis Project"]
    },
    "SQL": {
        "next": "Power BI",
        "time": "3 weeks",
        "resources": ["SQL Tutorial", "YouTube SQL"],
        "projects": ["Database Analysis"]
    },
    "Power BI": {
        "next": "Statistics",
        "time": "3 weeks",
        "resources": ["Power BI Docs"],
        "projects": ["Dashboard Project"]
    },
    "Statistics": {
        "next": None,
        "time": "3 weeks",
        "resources": ["Statistics Course"],
        "projects": ["Business Data Report"]
    }
}

data_analyst_meta = {
    "roles": ["Data Analyst", "Business Analyst"],
    "resources": ["Kaggle", "Coursera", "YouTube"],
    "time": "5-8 months",
    "demand": "High",
    "salary": "5 - 18 LPA"
}

data_analyst_career = BaseCareer(
    "Data Analyst",
    data_analyst_graph,
    data_analyst_meta
)

# ---------------- BACKEND CAREER ----------------


backend_graph = {

    "Python": {
        "next": "APIs",
        "time": "3 weeks",
        "resources": ["Python Docs", "freeCodeCamp"],
        "projects": ["CLI Tool", "File Parser"]
    },

    "APIs": {
        "next": "Databases",
        "time": "2 weeks",
        "resources": ["REST API Tutorials"],
        "projects": ["Simple REST API"]
    },

    "Databases": {
        "next": "Django/Flask",
        "time": "3 weeks",
        "resources": ["SQL Docs"],
        "projects": ["User Database System"]
    },

    "Django/Flask": {
        "next": "Deployment",
        "time": "4 weeks",
        "resources": ["Django Docs"],
        "projects": ["Blog Backend"]
    },

    "Deployment": {
        "next": None,
        "time": "2 weeks",
        "resources": ["Docker Tutorials"],
        "projects": ["Deploy Web API"]
    }
}

backend_meta = {
    "roles": ["Backend Developer"],
    "resources": ["YouTube"],
    "time": "6-8 months",
    "demand": "High",
    "salary": "5 - 18 LPA"
}

backend_career = BaseCareer(
    "Backend Developer",
    backend_graph,
    backend_meta
)

# ---------------- DATA ANALYST CAREER ----------------

data_analyst_graph = {
    "Python": {
        "next": "Pandas",
        "time": "3 weeks",
        "resources": ["YouTube Python", "freeCodeCamp"],
        "projects": ["Data Cleaning Project"]
    },
    "Pandas": {
        "next": "SQL",
        "time": "3 weeks",
        "resources": ["Pandas Docs", "Kaggle"],
        "projects": ["Data Analysis Project"]
    },
    "SQL": {
        "next": "Power BI",
        "time": "3 weeks",
        "resources": ["SQL Tutorial", "YouTube SQL"],
        "projects": ["Database Analysis"]
    },
    "Power BI": {
        "next": "Statistics",
        "time": "3 weeks",
        "resources": ["Power BI Docs"],
        "projects": ["Dashboard Project"]
    },
    "Statistics": {
        "next": None,
        "time": "3 weeks",
        "resources": ["Statistics Course"],
        "projects": ["Business Data Report"]
    }
}

data_analyst_meta = {
    "roles": ["Data Analyst", "Business Analyst"],
    "resources": ["Kaggle", "Coursera", "YouTube"],
    "time": "5-8 months",
    "demand": "High",
    "salary": "5 - 18 LPA"
}

data_analyst_career = BaseCareer(
    "Data Analyst",
    data_analyst_graph,
    data_analyst_meta
)





# ---------------- REGISTRY ----------------



career_registry = {
    "Frontend Developer": frontend_career,
    "Data Analyst": data_analyst_career,
    "AI/ML Engineer": ai_career,
     "Backend Developer": backend_career,
    "Cloud Engineer": cloud_career,
    "DevOps Engineer": devops_career,
    "Cybersecurity Analyst": cyber_career,
    "Power BI Expert": powerbi_career,
    "Product Manager": product_career
}

def generate_career_roadmap(interest, skills):

    career_obj = career_registry.get(interest)

    if not career_obj:
        return None

    return career_obj.generate(skills)