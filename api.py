from sounds import *

@app.route('/<string:sound_type>/<int:id>', methods=['GET'])
def get_sounds(sound_type,id):
    '''Function to get all the movies in the database'''
    song=Song()
    return jsonify({'Movies': song.get_all_songs()})


if __name__ == "__main__":
    app.run(port=1234, debug=True)