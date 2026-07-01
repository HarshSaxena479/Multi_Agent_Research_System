from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url

load_dotenv()


# =========================
# LLM Setup
# =========================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# =========================
# Search Agent
# =========================

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )


# =========================
# Reader Agent
# =========================

def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )


# =========================
# Writer Chain
# =========================

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert research writer.

        Write clear, structured, professional,
        and fact-based research reports.
        """
    ),
    (
        "human",
        """
        Write a detailed research report.

        Topic:
        {topic}

        Research:
        {research}

        Structure:

        1. Introduction

        2. Key Findings
           - Minimum 3 detailed findings

        3. Conclusion

        4. Sources
           - Include every URL referenced

        Be professional and comprehensive.
        """
    ),
])

writer_chain = writer_prompt | llm | StrOutputParser()


# =========================
# Critic Chain
# =========================

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert research critic.

        Analyze reports objectively.
        Identify strengths, weaknesses,
        factual gaps and missing details.
        """
    ),
    (
        "human",
        """
        Review the report below.

        Report:
        {report}

        Respond EXACTLY in this format:

        Score: X/10

        Strengths:
        - ...
        - ...

        Areas to Improve:
        - ...
        - ...

        One Line Verdict:
        ...
        """
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()