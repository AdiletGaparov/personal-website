---
<div class="">   

**Final project for Natural Language Processing (NLP) class at IE: Application of NLP**

**Title**   
Sentimental Music Box

**Overview**   
Our app recommends songs to students based on sentiment and subjectivity of lyrics. 
Inspired by why and how recommendation engines bring value (we had a separate class on it) to users and how Spotify nailed it with Discover Weekly and other custom playlists, we decided to build our own music streaming service for a segment of users we knew a lot at that time: *students*.

While the majority of recommendation systems in production are based on users' collective usage (Collaborative Filtering), we know that the state-of-art systems, deployed by Spotify as an example, take into account the content (lyrics/rhythm). We hypothesized that for students, who prepare for exams, the lyrics itself will bring the most value. 

Our idea relies on unveiling and categorizing songs based on the emotions and subjectivity that are transmitted by the lyrics of the song and not by its rhythm. Check *Alors on danse* by Stromae, which people loved to dance to:

> Original: 
>> Et là tu te dis que c'est fini car pire que ça ce serait la mort
>
>> Quand tu crois enfin que tu t'en sors, quand y en a plus et ben y en a encore

> Translation:
>> And then you tell yourself it's over because worse than that it would be death 
>
>> When you finally believe that you get out of it, when there is more and well there is still

**Objectives**
* Test the hypothesis that content-based recommendations are valuable in certain use cases
* Test the application of current libraries, used in sentiment analysis (text analytics)

**Success metrics**
* [Potential] Usage, measured by the feedback of the class ("Raise your hand if you'd use it?")
* Accuracy of sentiment analysis, measured by the feedback from the class

**Messaging**   
Prepare your mind for flow state during studying by listening to appropriate music.

**Persona(s)**   
A university student                                                                                                                                    

**User scenarios**  
A student named Alen is planning to study for an exam on Machine Learning. It is really important one, but there are so many things going on in his head. Moreover, he is not really prepared, but the exam is scheduled for next week and he starts to feel a little bit desperate.
Alen decides to listen to music to block outside noise and better concentrate, he opens the music app, chooses the subject he is planning to study now, the level of readiness, and general genre he prefers. The app shows him the list of songs. Alen now can add songs to his playlist and start listening and prepare himself for the upcoming exam. 

**User Stories/Features/Requirements**:    
* As a student, I want to add songs to my playlist so that I can listen to songs that I chose without interruption.
* As a student, I want to choose subject I am preparing for so that I can listen to music that is more relevant for this subject.
* As a student, I want to choose genre of music so that I can listen to favourite genre.
* As a student, I want to choose how well I am prepared so that I can listen to songs with lyrics whose meaning will be more relevant.

**Q&A**   
* We used [TextBlob](https://textblob.readthedocs.io) for sentiment analysis. It gives two values for a text: Polarity and Subjectivity. Polarity value ranges from -1 (negative sentiment) to +1 (positive sentiment). Subjectivity value ranges from 0 (very objective) to 1 (very subjective). You can test this library on the navigation panel under Tech Demo (👈).
* We hypothesized that when a student is studying hard science (i.e. Math or Python), her mind needs to adapt to objectivity and therefore our app suggests songs whose lyrics are estimated to be objective (Subjectivity is closer to 0). On the contrary, when she studies for soft science (i.e. Ethics or Literature), we think that songs with very subjective lyrics will help in creativity and expressing her own opinion.   
* We hypothesized that when a student is desperate (because not prepared enough given the time until the next exam), her mind needs songs with positive words, therefore our app suggests songs with Polarity closer to 1. On the contrary, if the student thinks she is ready, our app suggests songs with more negative polarity to balance out the excessive optimism. 
* For the MVP web app, we used MetroLyrics database of lyrics, downloaded from Kaggle. 
* We tailored the UI for our Master in Business Analytics & Big Data program at IE.

**Designs**   
Below there is UI of the web app I built (not perfect, but does the job with my basic knowledge of JavaScript).
</div>