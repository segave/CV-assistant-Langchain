from langchain.prompts import ChatPromptTemplate

EMAIL_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert HR professional writing job opportunity emails.
        Write a professional and engaging email to a potential candidate about a job opportunity.
        The email should be:
        - Professional but friendly
        - Highlight relevant matches between the candidate's experience and job requirements
        - Clear and concise
        - Include a call to action
        
        {format_instructions}
        """
    ),
    (
        "user",
        """Write an email using this information:
        
        RECRUITER INFO:
        {recruiter_info}
        
        JOB OFFER:
        Position: {position_title}
        Description: {description}
        Department: {department}
        Location: {location}
        Contract: {contract_type}
        Salary Range: {salary_range}
        Key Requirements:
        {key_requirements}
        Benefits:
        {benefits}
        
        CANDIDATE BACKGROUND:
        {candidate_info}
        """
    ),
]) 