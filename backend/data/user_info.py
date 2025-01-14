class UserInfo:
    # HR Professional Information
    FULL_NAME = "John Doe"
    POSITION = "HR Assistant"
    COMPANY = "Colmena AI"
    EMAIL = "john.doe@colmena.ai"
    PHONE = "+34 600 000 000"
    SIGNATURE = f"""
Best regards,
{FULL_NAME}
{POSITION} at {COMPANY}
{EMAIL}
{PHONE}
"""


class JobOffer:
    # Current Job Opening Information
    POSITION_TITLE = "Senior Software Engineer"
    DEPARTMENT = "Engineering"
    LOCATION = "Madrid, Spain (Hybrid)"

    # Job Details
    DESCRIPTION = """
We are looking for a Senior Software Engineer to join our growing team at Colmena AI. 
The ideal candidate will have strong experience in:
- Backend development with Python
- Cloud services (AWS/Azure)
- AI/ML implementation
- Team leadership
"""

    REQUIREMENTS = [
        "5+ years of experience in software development",
        "Strong Python programming skills",
        "Experience with cloud services (AWS/Azure)",
        "Knowledge of AI/ML frameworks",
        "Excellent communication skills",
        "Fluent in English (Spanish is a plus)",
    ]

    BENEFITS = [
        "Competitive salary",
        "Flexible working hours",
        "Remote work options",
        "Health insurance",
        "Continuous learning budget",
        "Stock options",
    ]

    SALARY_RANGE = "€45,000 - €65,000"
    CONTRACT_TYPE = "Full-time, Permanent"

    @classmethod
    def get_full_description(cls) -> str:
        """Returns a formatted full job description"""
        return f"""
Position: {cls.POSITION_TITLE}
Department: {cls.DEPARTMENT}
Location: {cls.LOCATION}
Contract: {cls.CONTRACT_TYPE}
Salary Range: {cls.SALARY_RANGE}

About the Role:
{cls.DESCRIPTION}

Requirements:
{"".join(f"- {req}\n" for req in cls.REQUIREMENTS)}

We Offer:
{"".join(f"- {benefit}\n" for benefit in cls.BENEFITS)}
"""
