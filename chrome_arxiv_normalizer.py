import appscript
app = appscript.app('Google Chrome')
for window in app.windows():
    for tab in window.tabs():
        url = tab().URL()
        if url.startswith('https://arxiv.org/pdf'):
            new_url = url.rstrip('.pdf').replace('pdf', 'abs')
            print(f'{url} -> {new_url}')
            tab.URL.set(new_url)
