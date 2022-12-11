from app import app, db

if __name__ == '__main__':
    try:
        print('Starting server')
        app.run(debug=False)
    except e:
        print(e)
    finally:
        db.close()
        exit()