from gtts import gTTS


def change_text(search_term , text_res):
    tts_en = gTTS(text_res, lang='en-uk')
    print('Audio')
    
    tts_en.save("wiki-videos\\images\\" + str(search_term) + '.mp3')  
    return ("wiki-videos\\images\\" + str(search_term) + '.mp3')

