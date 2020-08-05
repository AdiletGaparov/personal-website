**Final project for Natural Language Processing (NLP) class at IE: Application of NLP**

**Disclaimer**: this is a group project, but the MVP web app was written by me using Flask (micro web framework written in Python), pure JavaScript, and SoundCloud API. You can find the code on my [GitHub](https://github.com/AdiletGaparov/sentiment-based-song-recommender).

We called our app "Sentimental Music Box", which recommends songs to students based on sentiment and subjectivity of lyrics. Inspired by why and how recommendation engines bring value (we had a separate class on it) to users and how Spotify nailed it with Discover Weekly and other custom playlists, we decided to build our own music streaming service for a segment of users we knew a lot at that time: *students*.

While the majority of recommendation systems in production are based on users' collective usage (Collaborative Filtering), we know that the state-of-art systems, deployed by Spotify as an example, take into account the content (lyrics/rhythm). We hypothesized that for students, who prepare for exams, the lyrics itself will bring the most value. 

Our  idea relies on unveiling and categorizing songs based on the emotions and subjectivity that are transmitted by the lyrics of the song and not by its rhythm. Check *Alors on danse* by Stromae, which people loved to dance to:

> Original: 
>> Et là tu te dis que c'est fini car pire que ça ce serait la mort
>
>> Quand tu crois enfin que tu t'en sors, quand y en a plus et ben y en a encore

> Translation:
>> And then you tell yourself it's over because worse than that it would be death
> 
>> When you finally believe that you get out of it, when there is more and well there is still



