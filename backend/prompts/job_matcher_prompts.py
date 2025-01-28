from langchain.prompts import ChatPromptTemplate

ANALYSIS_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert HR recruiter analyzing candidate matches for a job position.
        Compare the candidates' profiles with the job requirements and provide a detailed analysis.
        Focus on:
        1. Overall match percentage
        2. Key matching skills and experience
        3. Potential areas for growth
        4. Recommendations
        
        Format your response clearly and concisely."""
    ),
    (
        "user",
        """Analyze these candidates for the following position:
        
        JOB REQUIREMENTS:
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
        
        CANDIDATES INFORMATION:
        {candidates_info}
        
        Provide a detailed analysis focusing on the match between each candidate's profile 
        and our specific job requirements. Include a match percentage for each candidate."""
    ),
]) 