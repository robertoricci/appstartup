mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

echo "\
[general]\n\
email = \"roberto.rricci@gmail.com\"\n\
" > ~/.streamlit/credentials.toml