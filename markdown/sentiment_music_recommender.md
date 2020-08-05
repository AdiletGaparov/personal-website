---
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

**Personas**: Who are the target personas for this product, and which is the key persona?

**User scenarios** These are full stories about how various personas will use the product in context.

**Requirements/features in**: These are the distinct, prioritized features along with a short explanation as to why the features are important. As a [type of user], I want to [perform some task] so that I can [achieve some goal]. 

**Features out**: What have you explicitly decided not to do and why? Designs: Include any needed early sketches, and link to the actual
designs once they’re available.

**Open issues**: What factors do you still need to figure out?

**Q&A**: What are common questions about the product, and answers to those questions? This is a good place to note key decisions.

**Other** considerations: This is a catch-all for anything else, such as if you make a key decision to remove or add to the project’s scope.

---
**Implementation:**

For this project, we used MetroLyrics database of lyrics, downloaded from Kaggle. To determine the sentiment and subjectivity of the lyrics


