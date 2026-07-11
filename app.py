import sys

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "cli"

    if mode == "cli":
        from views.cli_view import run
        run()
    elif mode == "web":
        from views.web_view import app
        app.run(host="0.0.0.0", debug=True)
    else:
        print("Usage: python app.py [cli|web]")

if __name__ == "__main__":
    main()