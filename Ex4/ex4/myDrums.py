import mySyth
class Drums:
  def play(self):
    print("playing the Drums")
    
drums=Drums()
mysynths=mySyth.Synth()
def play_instrument(instrument):
  instrument.play()


play_instrument(drums)
play_instrument(mysynths)

  
  