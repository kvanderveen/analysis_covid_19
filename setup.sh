mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"kevin.r.vanderveen@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml