from app import app, db

if __name__ == '__main__':
    try:
        print('Starting server')

        # production server
        from waitress import serve
        serve(app, host="0.0.0.0", port=3001)

        # development server (Port 5000)
        # app.run(debug=False)
    except e:
        print(e)
    finally:
        db.close()
        exit()