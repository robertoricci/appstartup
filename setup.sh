kdir -p ~/.streamlit/
echo "
[server]n
headless = truen
port = $PORTn
enableCORS = falsen
n
" > ~/.streamlit/config.toml