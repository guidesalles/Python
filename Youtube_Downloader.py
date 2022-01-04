from pytube import YouTube

url = input("Qual URL do vídeo? ")

YouTube(url).streams.get_highest_resolution().download()