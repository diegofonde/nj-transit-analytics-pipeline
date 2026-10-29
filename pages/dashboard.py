import streamlit as st
import streamlit.components.v1 as components

st.title("Interactive Tableau Dashboard 📊")

tableau_embedded = """
<div class='tableauPlaceholder' id='viz1793284572737' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;nj&#47;nj_transit&#47;NJTransitExecutiveOperationsOverview&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='nj_transit&#47;NJTransitExecutiveOperationsOverview' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;nj&#47;nj_transit&#47;NJTransitExecutiveOperationsOverview&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1793284572737');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1657px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='901px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1657px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='901px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1500px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
components.html(tableau_embedded, height = 851, width = 1657,scrolling = True)

st.markdown("""
    Welcome to the data visualization hub! This page features an interactive Tableau dashboard hosted on Tableau Public. 
    The page features 3 main dashboards, 
""")