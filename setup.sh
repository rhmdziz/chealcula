mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"23502210001@student.prasetiyamulya.ac.id\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml