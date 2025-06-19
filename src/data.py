from models import db, User, Artist, Album, Song

def registrar_artistas():
    artists = [
            {
                "name": "Kendrick Lamar",     
                "description": "Kendrick Lamar Duckworth (born June 17, 1987) is an American rapper. Regarded as one of the most influential hip-hop artists of his generation, and one of the greatest rappers of all time, he was awarded the 2018 Pulitzer Prize for Music, becoming the first musician outside of the classical and jazz genres to receive the honor. Born in Compton, California, Lamar began releasing music under the stage name K.Dot while attending high school. He signed with Top Dawg Entertainment (TDE) in 2005.", 
                "image": "https://cdn-images.dzcdn.net/images/artist/be0a7c550567f4af0ed202d7235b74d6/500x500-000000-80-0-0.jpg",
                "genre": "rap",
                "listeners": "83627314",
            },
            {
                "name": "The Weeknd",     
                "description": "Abel Makkonen Tesfaye, popularly known as The Weeknd (born February 16, 1990 in Toronto, Ontario, Canada), is a Canadian R&B/hip-hop musician, singer-songwriter and record producer. He chose his stage name in tribute to when he was 17 years old, when, along with his friend La Mar Taylor, he dropped out of high school, took his mattress, and left one weekend and never came home. However, his estranged former producer Jeremy Rose claims the name was his idea.", 
                "image": "https://cdn-images.dzcdn.net/images/artist/581693b4724a7fcfa754455101e13a44/500x500-000000-80-0-0.jpg",
                "genre": "pop",
                "listeners": "113090717",
            },
            {
                "name": "Lady Gaga",     
                "description": "Stefani Joanne Angelina Germanotta, known professionally as Lady Gaga, (born March 28, 1986 in New York, NY) is an American singer, songwriter and actress. She is known for her image reinventions and musical versatility. Gaga began performing as a teenager, singing at open mic nights and acting in school plays. She studied at Collaborative Arts Project 21, through the New York University Tisch School of the Arts, before dropping out to pursue a career in music.", 
                "image": "https://cdn-images.dzcdn.net/images/artist/7565262f7661b0d762621a8d69ba6f49/500x500-000000-80-0-0.jpg",
                "genre": "pop",
                "listeners": "107615296",
            },
            {
                "name": "Linkin Park",     
                "description": "Linkin Park are an American rock band from Agoura Hills, California. The band's current lineup comprises of vocalist/rhythm guitarist/keyboardist Mike Shinoda, lead guitarist Brad Delson, bassist Dave Farrell, DJ/turntablist Joe Hahn, drummer Colin Brittain, and lead vocalist Emily Armstrong. Shinoda, Delson, Farrell and Hahn are founding members. Vocalists Mark Wakefield, Chester Bennington & drummer Rob Bourdon are former members of the band. Categorized as alternative rock", 
                "image": "https://cdn-images.dzcdn.net/images/artist/4886905210739af3438990897bad3a98/500x500-000000-80-0-0.jpg",
                "genre": "rock",
                "listeners": "50675885",
            },
            {
                "name": "Taylor Swift",
                "description": "Taylor Swift (born December 13, 1989) is an American singer-songwriter whose work spans country, pop, indie folk and more. She’s one of the most awarded and best‑selling artists in history, with 14 Grammy Awards and record-breaking streaming numbers worldwide.",
                "image": "https://cdn-images.dzcdn.net/images/artist/d37ef92e54376529cc956a270827dd49/500x500-000000-80-0-0.jpg",
                "genre": "country",
                "listeners": "82913915",  
            },
            {
                "name": "Eminem",
                "description": "Marshall Mathers, known as Eminem (born October 17, 1972), is an American rapper, songwriter and record producer. He is among the best‑selling rappers ever, with multiple Grammy Awards and widely praised for his lyrical skill and cultural impact.",
                "image": "https://cdn-images.dzcdn.net/images/artist/19cc38f9d69b352f718782e7a22f9c32/500x500-000000-80-0-0.jpg",
                "genre": "rap",
                "listeners": "67452090",  
            },
            {
                "name": "Coldplay",
                "description": "Coldplay is a British rock band formed in 1996, known for their melodic, anthemic sound and global stadium tours. They have won multiple Grammys and have several songs with over a billion streams each.",
                "image": "https://cdn-images.dzcdn.net/images/artist/3087954bca22f306324912e5ac8375c3/500x500-000000-80-0-0.jpg",
                "genre": "rock",
                "listeners": "92854366",  
            },
            {
                "name": "Paramore",
                "description": "Paramore is an American rock band formed in 2004, fronted by Hayley Williams. They’re known for energetic pop-punk and emo-influenced hits like “Misery Business” and “Ain’t It Fun”.",
                "image": "https://cdn-images.dzcdn.net/images/artist/60dc1956a36a5e552384b4a32b0cbf9b/500x500-000000-80-0-0.jpg",
                "genre": "rock",
                "listeners": "28026843", 
            },
            {
                "name": "Red Hot Chili Peppers",
                "description": "Red Hot Chili Peppers is an American rock band from Los Angeles, formed in 1983. They blend rock, funk and punk, and are known for hits like “Californication” and “Under the Bridge”.",
                "image": "https://cdn-images.dzcdn.net/images/artist/238f5524a401dfdd5cac685f0f7989bd/500x500-000000-80-0-0.jpg",
                "genre": "rock",
                "listeners": "40552983",
            },
            {
                "name": "Ariana Grande",
                "description": "Ariana Grande (born June 26, 1993) is an American pop and R&B singer known for her powerful vocals and string of hits like “7 Rings” and “Thank U, Next”. She’s among Spotify’s most-followed female artists. ",
                "image": "https://cdn-images.dzcdn.net/images/artist/5fcde7fde7cde95fc36d4576afcfb49f/500x500-000000-80-0-0.jpg",
                "genre": "pop",
                "listeners": "79027289",  
            },
            {
                "name": "Billie Eilish",
                "description": "Billie Eilish (born December 18, 2001) is an American singer-songwriter whose dark, minimalist pop sound and intimate vocals gained her Grammy sweeps and a large younger fanbase.",
                "image": "https://cdn-images.dzcdn.net/images/artist/8eab1a9a644889aabaca1e193e05f984/500x500-000000-80-0-0.jpg",
                "genre": "pop",
                "listeners": "97175247", 
            },
            {
                "name": "The Smiths",
                "description": "The Smiths was an English rock band formed in Manchester in 1982, fronted by Morrissey. They became icons of ’80s indie rock and are celebrated for their poetic lyrics and jangly guitar sound.",
                "image": "https://cdn-images.dzcdn.net/images/artist/458e4ee61a7fc57a79ac2b9b20c47bd9/500x500-000000-80-0-0.jpg",
                "genre": "indie",
                "listeners": "18554356",
            },
            {
                "name": "The Neighbourhood",
                "description": "The Neighbourhood is an American alternative rock band from California, best known for their hit “Sweater Weather”. Their music blends moody indie, R&B and electronic influences.",
                "image": "https://cdn-images.dzcdn.net/images/artist/b9baaa2d9485a510cb868a8de6a7adc6/500x500-000000-80-0-0.jpg",
                "genre": "indie",
                "listeners": "39725563",
            },
            {
                "name": "The Killers",
                "description": "The Killers is an American rock band formed in Las Vegas in 2001. They gained fame with anthemic hits like “Mr. Brightside” and “Somebody Told Me” and are known for their energetic rock sound.",
                "image": "https://cdn-images.dzcdn.net/images/artist/979d671d4b391bc07747bd1569e51997/500x500-000000-80-0-0.jpg",
                "genre": "rock",
                "listeners": "25842220",
            },
        ]
    
    data_to_db = []
    for artist_data in artists:
        new_artist = Artist(
                name=artist_data["name"],
                description=artist_data["description"],
                image=artist_data["image"],
                genre=artist_data["genre"],
                listeners=int(artist_data["listeners"]),
            )
        data_to_db.append(new_artist)
    
    return data_to_db