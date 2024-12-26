# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:15:50 2024

@author: om
"""
#2
"""
We take the users review of 'Aladdin' movie
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://www.imdb.com/title/tt6139732/reviews/?ref_=tt_urv"
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
#prettify() function which removes all unnecessary data 
#movie reviews:
title = soup.find_all('a',class_="title")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
#in this review title we do not get purified reviews hense we can remove '\n' from it
review_title[:]=[title.strip('\n') for title in review_title]
review_title
#Here we get all reviews of movie
"""
[" This live action version of Disney's Aladdin was enjoyable enough on its own if one hasn't previously seen the studio's animated version",
 ' A whole new (different, but familiar) world....',
 " It's a really good movie",
 ' So much autotune.',
 ' Great visuals and all, but missing that "magic"',
 ' Better than expected',
 " Don't believe the put downs !",
 ' Funny and Entertaining Version by Guy Ritchie',
 ' Very Enjoyable!',
 ' Honest',
 ' My neck hurts',
 " I don't understand why the critics are bashing on this one.",
 ' on a magic carpet ride, well',
 ' Sadly, it met my expectations',
 " It's funny! It's rhythmic!! It's spectacular!!!",
 ' Aladdin lacks real magic',
 ' Solid Disney Movie. Entertaining.',
 ' Seriously what is wrong with critics I loved this retailing',
 ' Amazing story',
 ' Thank goodness for Disney+',
 " Good, but doesn't have the magic of the original",
 ' I thought it would never end',
 ' Enjoyable',
 ' Great Graphics',
 ' Disney sadly misses the mark... again.']
"""
len(review_title)
#total reviews title are 25
#now we find rating of movie
rating = soup.find_all('span',class_='point-scale')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('/') for r in rate]
rate
"""['10','10','10','10','10','10','10','10','10',
 '10','10','10','10','10','10','10','10','10','10','10',
 '10','10','10']
"""
len(rate)
#total rate is 23
#so we pop 2 reviews so we get 25
for i in range(0,2):
    rate.append(i)
len(rate)
#now we get total 25 rating
#now we extract the review body
review=soup.find_all('div',class_='text')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body

"""
['Having not previously seen the Disney-animated version of Aladdin-just choice clips usually featuring the Robin Williams-voiced Genie-I do understand this Disney-live-action version is mostly the same sequence of events with the same songs with one addition. So on that note, I very much enjoyed this with my movie theatre-working friend. Will Smith is amusing enough as the Genie now and when the more dramatic scenes come, I was touched enough by the story, characters, and the actors playing them. And those songs are, of course, as awesome as ever! So on that note, I recommend this version of Aladdin.',
 'As soon as this live action version of Aladdin was first announced, it seems certain people were against it. While I too have fond memories of seeing the original animated version at the theatre, I was at least willing to give this one a chance. I\'m glad I did. Firstly, people need to realise an animated film and live-action film are two different things. Some things that work in animation just won\'t translate too well into live-action. The other thing to accept is that, short of resurrecting Robin Williams, there was no way they were ever going to be able to replicate his unique take on the character of the Genie. Once you open your mind to the possibility that something can be \'different\' but also *good*; then you\'ll have a more pleasant experience. That\'s what we get here: a movie that is familiar, but at the same time new/different (and that\'s not a bad thing).From the very beginning, the movie is somewhat different to what we might be expecting when we\'re introduced to who is telling the story. While it was immediately evident to me what was going on, it wasn\'t a \'bad\' addition. After sweeping shots set to the song \'Arabian Nights\', we\'re introduced to the \'street rat\' named Aladdin. Although much fuss has been made about the Genie casting, if Aladdin had been miscast, then the whole film would\'ve suffered. Thankfully, I can say that I almost immediately liked Mena Massoud in the role. He\'s funny, got moves/charm, makes for a likeable \'thief\' and his relationship with his pet monkey, Abu, is as good as I\'d hoped it\'d be. Speaking of, although people think of CGI characters badly a lot of the time, it must be made clear the animal companions in this are all wonderfully brought to life/fully-realised characters. Abu is expressive, funny, and helpful (despite sometimes getting them both into trouble).Not before long Aladdin encounters Princess Jasmine (a well-cast Naomi Scott, who does a lot with the character and should make most Jasmine fans proud), who\'s undercover among the people. I was afraid that the movie would rush through their first meeting, but was happy with the amount of time devoted to them developing an interest in each other. I could instantly tell that the beloved character of Jasmine was in safe hands as portrayed by Naomi Scott and that she had nice chemistry with Massoud\'s Aladdin. Although not given as much to do as Abu, Jasmine\'s loyal tiger companion, Rajah, is another lovely animal created with CGI, who I appreciated wasn\'t largely ignored. Jasmine\'s other loyal friend, her handmaiden named Dalia, is actually a stand-out character in the movie. Nasim Pedrad has excellent comic timing, as does Naomi Scott, which is on full display in a fun scene where Aladdin comes to the palace and Jasmine attempts to maintain her cover.The one \'miss\' in the casting department is that of Marwan Kenzari as villainous Jafar. While others had pre-judged him based on the trailers alone, I was willing to give him a chance to make up for his lack of sinister voice with what would hopefully be at least a menacing performance. Sadly, he lacks even that. There\'s nothing particularly memorable about his portrayal (even near the end when he\'s given every opportunity to unleash in full-on villain mode, he falls way short). About the only \'positive\' I could find regarding his character is his animal companion of Iago. The red parrot might not be quite as talkative as the animated version, but he *does* talk (and in a much more bird-like way), getting a few funny lines here and there (I\'d expect nothing less from Alan Tudyk providing the voice). It\'s just disappointing that Jafar\'s miscast, and thus the \'weak link\' in the film.What most people are probably wondering about is Will Smith as the Genie. I actually thought he was pretty good here (and I found him more likeable in this role than I have in any movie I\'ve seen him in since probably the first Men In Black). There are just one or two instances where I felt he tried to emulate Robin Williams\' version and it didn\'t quite work, but on the whole I felt he brought his own energy/style to the character of Genie and it (mostly) worked. The most important thing was the friendship that he formed with Aladdin. While Smith\'s Genie may seem a bit more snarky than you might expect, when it comes to the emotional beats, his performance hits the right notes (especially near the end).Speaking of notes, "What about the songs?" you may ask. I was pretty happy with them, there were just the right amount and they didn\'t feel particularly intrusive in any of the scenes they were featured. Even the new song, \'Speechless\', isn\'t too bad (though there are those who\'ll no doubt complain). Massoud and Scott have really nice singing voices and did their songs justice, I thought. Will Smith\'s also decent with his main songs in the movie (the end credits one I could\'ve done without, though).I must also praise the costumes (Jasmine\'s are all stunning, as is Jasmine herself), the use of vibrant colours is quite impressive and the overall look of the film feels like something new/different to what we\'ve seen time and time again in films (especially Disney ones). Things I forgot to mention: the Magic Carpet has as much \'character\' as in the original (I especially appreciated seeing how close friends Carpet and Abu became by the end), and even the Sultan\'s head guard, Hakim, is given some depth.In conclusion, if you go into the theatre already disliking/hating the film based on just the trailers, then you\'re probably going to leave the same way you entered: bitter and thinking things like "It ruined my childhood!" (such a rubbish statement). Just try accepting this is a different thing and hopefully you\'ll enjoy it.',
 "I watched this movie this morning and it's beautiful. The original animation is better but it's a little good movie. Will Smith is amazing as the genie. I loved it.",
 'I was left cringing during each musical sequence due to the blatant over use of autotune. The actors bring no emotion to the story.',
 'When it comes to visuals, through out the movie was just... beautiful- the clothes, culture and architecture. Will Smith\'s Genie was unexpectedly good and created his OWN version which is great! As for the rest of the major characters? Well...Jaafar was a bit of a let down from the beginning. Not menacing enough on the outside. Yet still cunning in some ways. Can\'t say much about his parrot... Jasmine\'s dad was disappointingly boring (prefer the bubbly albeit blur cartoony-version). Jasmine herself was alright (neither great nor terrible). The "feminist" like scenes were like an unecessary extra and a bit annoying to watch (don\'t ask me why). Abu (monkey) was cute. He was captured nicely. And lastly Aladdin? For a break through actor, he actually did a good job portraying Aladdin. EXCEPT his relationship with Jasmine.....And THAT\'S where the "magic" is missing. The core lovey-dovey magic thats hard to explain except through emotions. I feel it\'s one of the major things that makes Disney\'s Aladdin.. "ALADDIN"! But I felt nothing from the "Whole New World" scene. No chemistry between the two "lovers". Even in other scenes...\nThis is similarly felt between Aladdin & Genie. Particularly towards the end. The lack of that "core" emotion is so disappointing that I couldn\'t enjoy the movie as a whole. It just felt more on how it looked rather how it SHOULD feel. I mean this is Aladdin! Where\'s the magic?',
 'Considering the director was having trouble and the studio was working against a well loved classic. Plus a few other things, they pulled of a watchable film. Still forgettable but watchable. Maybe I am super impressed by this film because of how awful Dumbo was. Who knows. But this is worth a watch.',
 "This is a lovely film, colourful and full of life. I enjoyed the animated one and I equally love this one. You don't need to compare live to animation, just enjoy the ride.Well worth watching.",
 '"Aladdin" is a very funny and highly entertaining version of the Arabian Nights´ tale by Guy Ritchie. First of all, Will Smith steals the film in the role of a Genie - most of his scenes could be included in the best moments of the movie. The beauty of Naomi Scott is impressive and shines. Marwan Kenzari performs the great villain Jafar with good performance. The small-thief Mena Massoud is a great and warm-hearted Aladdin. Last but not the least, the monkey Abu and the evil macaw complete the brilliant cast of this good version indicated as a wonderful family entertainment. My vote is seven.Title (Brazil): "Aladdin"',
 "I know everyone wants to compare this to the Animated version, but don't. Take it as it comes and you will thoroughly enjoy it. It does stay pretty faithful to the animated version I think. Will Smith as the genie could never be the Robyn Williams genie, but I don't think he tries to. He does fantastically well in his own right. Absolutely loved the Prince Ali song where Aladdin enters the city as the prince. Brilliantly colorful spectacle captured really well. Jafar missed a little for me as had lost the smarmy-ness of the animated version. The songs were great and the Aladdin and Jasmine characterization was pretty spot on. I think kids would love this and I would definitely recommend it.",
 "The graphics: 9/10\nThe acting : 6/10 you know why :)\nThe story : 9/10\nMusic : 10/10\nMovie quality : 8/10\nmovie was great, their acting was good, the movie was funny, the tale is exactly on the point, I didn't like jafars acting, they could've replaced him with someone with evil face features, he seemed to be calm all the time. The other actors actually did great. I'm not going to spoil the ending, but it was better than the animated one.Does it deserve a try, Yes/ No?Yeah, give it a try and ignore negative reviews from the othersP.s. Well Smith did great in this movie",
 "I fell asleep the wrong way watching this. The unexpectedly long runtime caught me by surprise. Acting is ok, Will Smith is very present in the movie and that works.Fun for a Sunday sleepy afternoon.Overall 5/10 just because they could've done it better.",
 "I honestly didn't know what I was going into and it was such a delightful surprise! It really exceeded my expectations and I had fun during the whole movie. Critics are really being harsh and I can't believe that beauty and the beast was more critically praised. The movie was so bland and boring while this one has so much energy and life to it. The characters had amazing chemistry with each other and the lines were delivered smoothly. The two things I was worried about that subsided as soon as the movie started are:\n1- Jafar's character: Marwan tries his best to make but the material he's given isn't strong enough. I wish they developed his character more. However, I didn't mind the change they did it with his character as it fits more with this version.\n2- Cultural representation: The trailers made the movie look like a production from bollywood. Not hating on the Indian culture, but it really annoyed me as Arab to see a Middle Eastern/Arabic folk tale that we all know long before Disney introduced it to the world to be represented in a fully different culture. Fortunately, the movie looks and feels way more Arabian such Arabic writings here and there, hearing some people speaking Arabic briefly, the names and appearance of the people of Agrabah and of course the amazing score! Although there are some slight hints of India/South Asia in the clothing and dancing, but I didn't mind that at all.I would've give it a 10 if the cinematography was better. This is my only issue with movie as it looked like high budget TV soap opera in some scenes.Don't miss on this one! You'll have fun.",
 'Greetings again from the darkness. Aladdin ... come on down! You are the next participant in Disney\'s ongoing mission for live-action remakes of their classic films. And rest easy fans, this time the mega-studio has done right by the original. Now that doesn\'t mean there aren\'t surprises. How about Guy Ritchie as director? How about a cast of mostly unknowns? How about modernized songs and even a new one sung by Jasmine? And it probably goes without asking, but how about a lot of CGI?Mena Massoud ("Tom Clancy\'s Jack Ryan") stars as Aladdin, and he gets to showboat early in the film and flash some parkour skills in the familiar and high-octane chase through the village. Aladdin, of course, is labeled a \'street rat\' and \'riff-raff\', but he\'s also charming, handsome, talented as a thief, and quite warm-hearted. He and his pet monkey Abu - or more accurately, partner in crime - are streetwise and work quite well together, both for theft and love.Naomi Scott (slated to star in the CHARLIE\'S ANGELS movie coming out later this year) is a beautiful and ambitious Princess Jasmine, who wants to succeed her father as Sultan of Agrabah, but is instead forced to choose between a steady stream of suitors - each a Prince, as required by law. Ms. Scott has a terrific singing voice and really gets to cut loose on the new woman power song "Speechless".The blue Genie is played by Will Smith, and this is what has fans of the beloved 1992 animated film so flustered. No, Will Smith is not Robin Williams, and few if any, could match the late great comedian for his energy and comedic flair. But Mr. Smith does a marvelous job of staying true to the original, while also adding his own style ... a style that works very well for comedy, music, and dramatic moments. He is not likely to disappoint anyone who has an open mind.So let\'s talk about the villain. Marwan Kenzari is Jafar, the man so dissatisfied with being number 2. Personally, I would have preferred a more intimidating bad guy, but given the tone of the film (more on that below), he\'s a solid fit. His sidekick and smart-aleck parrot Iago is voiced by Alan Tudyk (it was the distinctive Gilbert Gottfried in the 1992 version). Two other key supporting roles include Nasim Padrad ("Saturday Night Live") as Dalla, Jasmine\'s handmaiden; and Navid Negahban (Abu Nazir in "Homeland") as the Sultan and Jasmine\'s father.It\'s been 27 years since Robin Williams\' Genie entertained so many, and the comparisons to that version are inevitable. It\'s a relief that Disney opted to keep the film family friendly (Rated PG) and avoid the dark tone that had their recent projects aimed more at adults than kids, rather than the balance they\'ve been known for more than 6 decades. Yes, this is the same director that made SNATCH (2000) and SHERLOCK HOLMES (2009), neither of which any decent parent would allow their young kids to watch. But, Mr. Ritchie has delivered a film which entertained (and didn\'t overly frighten) kids as young as 5 in the screening I attended.Director Ritchie co-wrote the script with John August, who is best known for his work with Tim Burton (BIG FISH, CHARLIE AND THE CHOCOLATE FACTORY, CORPSE BRIDE, DARK SHADOWS, FRANKENWEENIE). The film runs 2 hours and 8 minutes, 38 longer than the 1992 film ... though it doesn\'t feel too long. Gemma Jackson\'s set design of Agrabah, the Palace, and the Cave of Wonders are all stunning, and then of course, there is the music. Alan Menken won an Oscar for ALADDIN (1992) and his music is back and modernized, and sounds wonderful ... especially "A Whole New World" and Jasmine\'s new song.\nWith a talented cast of Arab/Middle Eastern/Central Asian/Southern Asian actors, there should be no cries of "foul", and there really is something special about a movie that can be thoroughly enjoyed by all ages. The Bollywood-type closing number provides a kaleidoscope of color, texture and dancing ... and is a nice twist to "You\'ve Never Had a Friend Like Me". And I\'ll leave you with this final offer: you can have the monkey, if I can have the magic carpet.',
 "What's to say. Before even filming we knew Guy Ritchie was obviously the wrong choice to direct the film. His style doesn't quite lend itself to this type of film.\nMiscast Mena Massoud didn't bring any real character to the role of Aladdin he was simply okay/ functional.\nWill Smith is as usual charismatic and had difficult shoes to fill after Robin Williams' take on the genie but he was seriously let down by the VFX in blue genie mode and a weak script.\nAnother miscast Naomi Scott gave a good performance but I always felt i was looking at Indian and not Middle Eastern. In fact the film IS very bollywood with the Jasmin, Aladdin dance off Indian Style (and to Indian music) then Russian dancing(?) plus other times an Indian soundtrack.\nAnd i'm not even going to talk about that sorry excuse for a villain. No, no i am not.\nFor a Disney movie set in large Kingdom it sure does feel quite quite small. It looked cheap too. Weird.\nUltimately a dreadfully executed cash grab of a movie that no one asked for. Thanks D.\nThankfully this is exactly what i expected having seen the trailers.",
 'Although this remake might seem less accomplished than the eponymous cartoon Aladdin (1992), the film is objectively well done. The actors, the songs, the sets, the costumes, the Computer-Generated Imagery (tiger, monkey, flying carpet, genie), ... everything is excellent!',
 "Even with a colossal budget and the spectacular tech available to Disney, live actors can't replicate the dizzy kinetics of a cartoon.",
 'Watched this movie with an open mind. There will NEVER be a Genie like Robin Williams but Will Smith definitely brings his own twist to being the Genie and it works. Fantastic music and dancing. Solid 7/10.',
 "Aladdin is the latest Disney remake based on the 1992 animated film starring the late Robin Williams. This 2019 retailing stars Will Smith, Mena Masound and Naomi Scott and follows the tale of a young man named Aladdin(Massound) who meets a young woman at the marketplace unaware that she is the Princess Jasmine in incongito(Scott)and wants to win her over. With help from a charming Genie(Will Smith),Aladdin disguises himself as a Prince. But when an evil sultan named Jafar wants the lamp,can Aladdin win the Princesses heart.Now I'm not gonna lie I was so nervous watching this film as I thought Will Smith would ruin it with his singing style and the other actors,but to my surprise along with my mom and my brother,we all loved it. Will Smith was great in this film with his comedic timing,Naomi Scott was excellent as Jasmine(And boy can she sing so good). The villian was decent I thought he was different compare to the 1992 version.The cinematography was gorgeous, the music was very good especially the new song Speechless. The costumes were stunning too.I loved how it wasn't a beat by beat of the original. For instance in the One Jump Ahead song Aladdin and Jasmine meet first thing while she is in incognito and near the end Jasmine didn't say I choose you Aladdin/call me Al.Guy Richie thank you for making this film. Would definetly put it in my top 5 favourite Disney Live Action movies of all time now.\nDefinetly buying this movie and may watch it in the cinemas again.9.5/10\nPs Mena Masound was handsome and likeable. His chemistry with Naomi Scott was perfect.",
 "A little bit more singing, but the movie was amazing. It's very hard to turn the legendary animation to movie, but by my opinion this was very successful. Enjoy and fun!",
 "I listened to people and didn't watch this when it first came out. I'm so glad I decided to turn this on when I got Disney+. What a fun movie! My niece loves all the colors, dances, and Will Smith's updated take on the genie!!!",
 "It's a good movie. Didn't really like the new songs. Acting was good. Jafar was miscast.",
 "I have only ever walked out of one movie before. This would have been the second one if it wasn't for the fact I was at the end of a row and didn't want to disturb two young families. It was so boring and yet should have been so good.There were so many chances missed. It's set in Arabia and yes the sets and scenery were amazing, but we never got a chance to enjoy them. The film kept skipping from scene to scene with little or no shots of anything apart from the actors. It should have and could have been both magical and beautiful. Couldn't we have seen Jasmin explore the city a little before bumping in Aladdin? That also would have made her character more rounded and show us how trapped she was in the palace.I totally fell in love with Aladdin from the animated film and had a teenage crush on him for years (yes, ok, he's an animated character I know, but don't judge me). This Aladdin lacked the animated version's spark and determination and worst of all kindness. He briefly hands a child some dates and that's about it. We don't get to see why he helps Jasmin in the market, it's all too rushed and so their relationship never really feels real and left me really not caring whether they ended up together or not.The songs, whilst sung quite well, didn't seem to fit into the film and every time one of them burst into song it felt false and like it had been crowbarred in.All in all it was a real disappointment and left me grieving for what might have been.",
 "I don't understand why this is getting a bashing? Based on the reviews I was expecting to hate this...not so, I thought it was a watchable enjoyable film.",
 "The movie was enjoyable. I watched it with my young grandchildren and they stayed still almost all the way through, so that's a plus. Nice storyline, great graphics. Lots of fun.",
 "Like many of the Disney live action adaptations, this film utterly fails to understand what made the original so great to begin with. Moments of character growth or interaction feel rushed and are changed up from the original, yet the outcome in the story still illogically remains the same. Some of the additional scenes around new characters simply feel laughable and out of place.\nThe additional song written for this film heavily clashes with the musical style of the existing ones and the instrumental accompaniment of the songs in general sounds too modern and not like a classical musical anymore.\nThe humor in this movie is very hit and miss. Some lines and moments are indeed extremely enjoyable, while most others seem too forced.\nThe VFX in this film are not entirely up to task and will undoubtedly look dated in a few years time. Most importantly, the overall spectacle feels much less impactful than the original's.\nOverall, there would be much more to go into. But this should be enough in summary."]

"""
len(review_body)
#total we get 25 reviews from review body
#now we have to save the data in .csv file
import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['Rate']=rate
df['Review']=review_body
df
#to create .csv file
df.to_csv("C:/8-text minning/text_mining/Aladdin_reviews.csv")
#############################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent = "This is a lovely film, colourful and full of life"
pol = TextBlob(sent).sentiment.polarity
pol
#0.425
df = pd.read_csv("C:/8-text minning/text_mining/Aladdin_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
"""
0     0.208333
1     0.206106
2     0.505357
3    -0.156250
4     0.133705
5     0.047500
6     0.383766
7     0.425000
8     0.299872
9     0.217188
10    0.075000
11    0.191447
12    0.224573
13   -0.049093
14    0.196667
15    0.359091
16    0.200000
17    0.351544
18    0.410417
19    0.494141
20    0.347273
21    0.036111
22   -0.150000
23    0.460000
24    0.121970
Name: polarity, dtype: float64
"""