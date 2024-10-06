input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showNumber(randint(1, 6))
    music.play(music.stringPlayable("E D C D E E E - ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("D D D - E G G - ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("E D C D E E E - ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("D D E D C C - - ", 150), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(200, music.beat(BeatFraction.Breve)), music.PlaybackMode.UntilDone)
})
