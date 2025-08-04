# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import Jogocobra.Jogo as Jogo
Jogo.init()
Jogo.mixer.music.load('torresmo_pt1-mp3cut.mp3')
Jogo.mixer.music.play()
Jogo.event.wait()
