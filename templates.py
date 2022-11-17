

def load_css() -> str:
    """ Return all css styles. """
    common_tag_css = """
                # display: inline-flex;
                # # align-items: center;
                # # justify-content: center;
                # padding: .15rem .40rem;
                # position: relative;
                # text-decoration: none;
                # font-size: 95%;
                # border-radius: 5px;
                # margin-right: .5rem;
                # margin-top: .4rem;
                # margin-bottom: .5rem;
    """
    return f"""
        <style>
       
        </style>
    """

def number_of_results(total_hits: int, duration: float) -> str:
    """ HTML scripts to display number of results and duration. """
    return f"""
        <div style="color:grey;font-size:95%;padding-left:270px">
           {total_hits} results ({duration:.2f} seconds)
        </div><br>
    """

def search_result( url: str,  **kwargs) -> str:
    """ HTML scripts to display search results. """
    return f"""
    <ol>
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<img id="img" src="{url}"  height="300px" width="650px" style="color:grey;font-size:95%;border-radius: 50px;" >
    
    </ol>
        
               
            
        
       
    """

