from agents import build_search_agent,build_reader_agent,writer_chain,critic_chain

def run_research_pipeline(topic:str) -> dict:
    state = {}
    
    # search agent working
    print("\n"+" ="*50)
    print("step1 - search agent is working....")
    
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [{
            "role": "user",
            "content": f"Find recent, reliable and detailed information about: {topic}"
        }]
    })
    
    content = search_result['messages'][-1].content

    state['search_results'] = (
        " ".join(block["text"] for block in content if block.get("type") == "text")
        if isinstance(content, list)
        else str(content)
    )
    
    print("\n search result",state['search_results'])
    
    # ste2 - reader agent
    print("\n"+" ="*50)
    print("step2 - reader agent is scraping top resources....")
    print("="*50)
    
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages":[{
            "role": "user",
            "content": (
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}"
            )
        }]
    })
    
    state['scraped_content'] = reader_result['messages'][-1].content
    
    print('\nScraped content\n',state['scraped_content'])
    
    #step-3 - Writer chain
    print("\n"+" ="*50)
    print("step3 - writer is drafting the report....")
    print("="*50)
    
    research_combined = (
        f"SEARCH RESULTS: \n {state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT: \n {state['scraped_content']}"
    )
    
    state['report'] = writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })
    
    print("\n Final report\n",state['report'])
    
    #Critic Report
    
    print("\n"+" ="*50)
    print("step4 - Critic is revewing the report....")
    print("="*50)
    
    state['feedback'] = critic_chain.invoke({
        "report":state['report']
    })
    
    print("\n Critic report\n",state['feedback'])
    
    return state
    
if __name__ == "__main__":
    topic = input("\nEnter research topic: ")
    run_research_pipeline(topic)