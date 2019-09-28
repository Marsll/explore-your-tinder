html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>Explore your Tinder</title>
                            <link rel="shortcut icon" type="image/x-icon" href="../static/img/favicon.ico">
                            {%css%}
                        </head>
                        <body>
                            <div class="header">
                                <nav class="navbar navbar-expand-md navbar-dark bg-dark">
                                    <div class = "container">
                                    <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">
                                        <a class="navbar-brand" href="/">
                                        <img src="../static/img/header_logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
                                        Explore Your Tinder
                                        </a>
                                    </div>
                                    <div class="navbar-collapse collapse w-100 order-3 dual-collapse2">
                                        <ul class="navbar-nav ml-auto">
                                            <li class="nav-item">
                                                <a class="nav-link" href="/about">About</a>
                                            </li>
                                        </ul>
                                    </div>
                                    </div>  
                                </nav>
                            </div>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''
