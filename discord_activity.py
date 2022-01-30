from pypresence import Presence
import time



RPC = Presence("")  #id аппликации в диске

btns = [
    {
        "label": "VK",
        "url": "https://vk.com"
    },
    {
        "label": "TG",
        "url": "https://tg.com"
    }
]

RPC.connect()
print("Ok")
RPC.update(
        state="Энтиной",#статус
        start=time.time(),#продолжительность активности
        buttons = btns,#кнопки
        large_image="bund",#имя основного изображения
        large_text="алхимим",#подпись при наведении на основное изображение
        small_image="unnamed",#имя дополнительного изображения
        small_text="опа, попався",#подпись  дополнительного изображения
        #party_id="smegma_id",
        #party_size=[1, 10],    #эти 3 строки добавляют кнопку присоеденится к активности
        #join ="smegma_connect" #чтобы воспользоваться закомментируйте строку buttons и раскоментируйте данные
)


while(True):        #пример анимации статуса
        RPC.update(
                state="эНтиной",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
            )
        time.sleep(1)
        RPC.update(
                state="энТиной",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
            )
        time.sleep(1)
        RPC.update(
                state="энтИной",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
        
        )
        time.sleep(1)
        RPC.update(
                state="энтиНой",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
        )
        time.sleep(1)

        RPC.update(
                state="энтинОй",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
        )
    
        time.sleep(1)
        RPC.update(
                state="энтиноЙ",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
        )
        
        time.sleep(1)
        RPC.update(
                state="энтиной.",
                start=time.time(),
                buttons = btns,
                large_image="bund",
                large_text="алхимим",
                small_image="unnamed",
                small_text="опа, попався",
                #party_id="smegma_id",
                #party_size=[1, 10],
                #join ="smegma_connect"
        )
        time.sleep(1)

    


