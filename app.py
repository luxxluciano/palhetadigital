# Import the required libraries
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Spotipy with client credentials
client_id = 'b83d9acaf62b4596ab9f819259196b9d'
client_secret = '889843d08c194f3fb7b3c7fde75921a8'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define a function to search for artists
def search_artist(artist_name):
    result = sp.search(artist_name, type='artist')
    return result['artists']['items']

# Define the main function of the app
def main():
    # Set the title of the app
    st.set_page_config(page_title='Spotify Artist Search')

    # Add a logo to the app in the same row as the title 'Palheta Digital' with sub header 'Strum Spotify Artists' to the app centerd in the row
    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:center; flex-direction:row;">
        <img src="https://i.pinimg.com/originals/1b/38/03/1b38032dc430e5eca87c6905cca05d11.png" style="width: 140px; height: 120px; margin-right: 10px;"/>
        <div style="display:flex; justify-content:center; align-items:center; flex-direction:column;">
            <h1 style="font-size: 30px; font-weight: bold; margin: 0px;">Palheta Digital</h1>
            <h2 style="font-size: 20px; font-weight: normal; margin: 0px;">Strum Spotify Artists</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

   

    # Create a text input for the user to enter the name of the artist
    artist_name = st.text_input('Enter the name of the artist')

    # If the user has entered an artist name
    if artist_name:
        # Search for the artist using the Spotify API
        results = search_artist(artist_name)

        # If no results were found, display a message to the user
        if not results:
            st.write(f'No results found for "{artist_name}"')
        else:
            # Get the first result
            artist = results[0]

            # Display the artist information and add a link to their Spotify page
            st.write(f'# {artist["name"]}')
            st.write(f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/{artist["uri"].split(":")[-1]}" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)

            # Display the other matching results in a gallery grid table of 8x4
            other_matches = results[1:]
            if other_matches:
                col1, col2, col3, col4 = st.columns(4)
                for i, artist in enumerate(other_matches):
                    if i < 8:
                        # Display artist information and add a link to their Spotify page
                        artist_name = artist['name']
                        artist_uri = artist['uri']
                        col = col1 if i % 4 == 0 else col2 if i % 4 == 1 else col3 if i % 4 == 2 else col4
                        with col:
                            st.write(f'{artist_name}')
                            st.write(f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/{artist_uri.split(":")[-1]}" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)

 #Add a line with 8 round buttons, passing  a unique key argument to 'st.button'  to make it work,  with the name of 
 #trending artists in spotify updated at page load that when clicked, display the artist information in evidence and
 #  the other similar matching results in a gallery grid table of 8x4 galery, make it with a for loop for scrape the artists names and pass it to the button function
  
    # Add footer text
    st.markdown("---")
    st.markdown("Powered by BananaMachinada")

# Run the app
if __name__ == '__main__':
    main()
