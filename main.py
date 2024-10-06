def on_gesture_shake():
    basic.show_number(randint(1, 6))
    music.play(music.string_playable("E D C D E E E - ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D D D - E G G - ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E D C D E E E - ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D D E D C C - - ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(200, music.beat(BeatFraction.BREVE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
