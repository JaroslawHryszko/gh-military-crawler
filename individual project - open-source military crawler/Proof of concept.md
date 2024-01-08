## Development of stand-alone open-source repositories (GitHub in first place) crawler which will analyze and detect Russian originated projects which could be used for military purposes;

#### The problem

Even though the conflict in Ukraine has been .... for almost 2 years, Russia does not stop and continues to attack the territory of its neighbor. On 29.12.2023, by [sending the biggest air attack since the start of the invasion](https://edition.cnn.com/2023/12/29/europe/ukraine-russia-airstrikes-intl-hnk/index.html), they killed at least 31 innocent people, and that's just one of their vicious attack that are probably to come.
Moreover, on the same day [a missile entered Polish airspace from Ukraine](https://notesfrompoland.com/2023/12/29/missile-that-entered-polish-airspace-likely-russian-says-warsaw/), most likely of a Russian origin, violating ..... (something, needs info), causing a disruption (disturbance) and scaring people because of a [similar event that took place last year, killing two people](https://notesfrompoland.com/2022/11/15/two-dead-in-explosion-amid-unconfirmed-report-of-russian-missiles-hitting-poland/).

Sadly, that means that the war is not going to end soon, and Ukraine is in need of help. 
(this part is ugly, change it)
Hence, the idea of the crawler.
#### Why? 

This paragraph is obvious - help people in Ukraine to defend themselves from Russia. If any open-source project is found using this crawler, it can possibly help defenders understand what their defense should be thanks to understanding the code behind e.g. rocket or drone pathing etc.

It's also possible that some other military [open-source intelligence (OSINT)](https://en.wikipedia.org/wiki/Open-source_intelligence) is found by that means of search:
- information about soldiers,
- their plans of attacks,
- maps etc.
	- *(...) researchers can i.a. develop geographical protection by visualising the area. Military reconnaissance focuses on information including: terrain, hydrographic networks, transport networks, land cover and the type of land. All this data is needed to develop a military strategy that often determines the success or failure of security systems.* - as stated [here](https://securityanddefence.pl/Open-source-intelligence-OSINT-as-an-element-of-military-recon,103337,0,2.html#S4)

#### Why can it be possible?

by Agata Ziółkowska in [*Open source intelligence (OSINT) as an element of military recon*](https://securityanddefence.pl/Open-source-intelligence-OSINT-as-an-element-of-military-recon,103337,0,2.html)

> (...) referring to OSINT as a form of military intelligence, because the inseparable association of intelligence with secrecy is one of the fundamental elements that distinguishes it from freedom of expression and demerging views.

(^ not here, delete that)


>For operational activities, publicly available and published information is crucial, i.e. about diplomatic activity and political plans that can be acquired through tools such as OSINT. This category also includes information on internal, economic, social, scientific and technical policies as well as demographic issues. Despite its openness, it is in the secret services’ scope, because after proper processing and analysis, it becomes valuable information (Dictionary of NATO).

// check how many russian repositories are there (if it's even possible)
// most popular military rockets, tanks, vehicles etc. - maybe a list from github or somewhere

- On GitHub we can find public organizations pointed at military research, like [DEVCOM Army Research Laboratory](https://github.com/USArmyResearchLab), or repositories, like [this one](https://github.com/ARL-UTEP-OC/ecel). 

- It's not uncommon that some student decides to publish their project and show to the world. It may happen that it is somehow [army-related](https://github.com/lrmcc/ARO-Senior-Design). Possibly it can contain some ___TOP SECRET___ data - mistakes happen. If that's not the case though, it still can be a foothold for further searching.

- Information leaks happen everywhere, and [this war is not the one avoiding it](https://www.nytimes.com/2023/04/08/us/politics/leaked-documents-russia-ukraine-war.html). What's best - the materials that were leaked were found on social media sites - it shouldn't be impossible for them to pop up somewhere on open-source repository hosts.

- 


#### Why it might not work?

Even though some open-source repositories are available, finding them among billions of others and filtering the right ones might be impossible.
We're also not sure if Russia uses any open-source repository hosts (of course it would be very dumb), like GitHub or GitLab - they probably have some self-hosted internal ones. If, however, the crawler finds some repositories, they might as well be filled with fake code/data to spread misinformation. 



>You cannot, however, bypass open sources with limited availability. Some portals and databases belong to these. Intelligence agencies are devoting more and more resources to obtaining information from the public. Unlimited access to content and a powerful amount of data requires appropriate selection in terms of topics and needs. Therefore, this type of operation uses specialised information technology

as stated [here](https://securityanddefence.pl/Open-source-intelligence-OSINT-as-an-element-of-military-recon,103337,0,2.html#S6)


### Key observations

Searching just in GitHub can be not enough since most of the serious leaks are revealed on dark web. Using one of [these crawlers/tools](https://medium.com/@tushar_rs_/dark-web-scraping-by-osint-scraping-tools-5e148e4eea0) (also [here](https://www.thedarkcrawler.com/)) could be beneficial to know how a military leak looks like and modify the search criteria. 
We could implement it by ourselves based on [*Crawling the Dark Web: A Conceptual Perspective, Challenges and Implementation*](https://www.researchgate.net/publication/332969272_Crawling_the_Dark_Web_A_Conceptual_Perspective_Challenges_and_Implementation) paper, but it might not be a good idea due to security reasons.

[War Thunder forum?](https://forum.warthunder.com/) - a lot of [military leaks](https://en.wikipedia.org/wiki/War_Thunder#Documents_leaks) happened there, but those were mostly specifications of tanks or aircraft.

https://vk.com - probably leaks can happen here as well

Maybe something from [this guy](https://github.com/cirosantilli)

Programming languages we're looking for:
- jets, rockets, drones etc.: 
	- ADA - [history of ADA on Stanford University site](https://cs.stanford.edu/people/eroberts/cs181/projects/1999-00/critical-systems/military.htm)and a [blogpost on `militaryembedded.com`](https://militaryembedded.com/avionics/software/ada-matters)
	- FPGA - [it's the official Intel site](https://www.intel.com/content/www/us/en/government/products/programmable/applications.html) (and the link contains `/us/government/`)
      - Verilog
      - VHDL
	- C/C++ 
		- [for aircrafts](https://aviation.stackexchange.com/a/15486)
		- [a paper on simulating military operations](https://arxiv.org/abs/2207.12084)
		- even some [weird GPT](https://chat.openai.com/g/g-0P9gf61T8) exists for military drone control in C++ for Canadian Armed Forces
      - Makefile 
    - Rust - the same reasons as above, but less likely to find in real military solutions - the software might be written by a guy who knows military and just doesn't like C++ (loves Rust for being *blazingly fast*)
- other military stuff, research etc.:
	- Java - [*Java, which has provided high productivity and quality in desktop and mobile applications, offers a compelling alternative to C++ for next-generation mission-critical systems*](http://pdf.cloud.opensystemsmedia.com/vita-technologies.com/Aonix.Jun07.pdf)
		- *Virtually all computer science and software engineering students are emerging from universities with training and expertise in Java, compared to relatively few Ada-trained graduates.*
	- Python - [*AI-enabled sensing radar gets FCC authorization*](https://militaryembedded.com/ai/cognitive-radar/ai-enabled-sensing-radar-gets-fcc-authorization), and if AI, then it's 99% that it is Python

-----
### What should we look for?

- any russian letters - in description, in `README.md`, in code - basically in any file
- probably mostly (if not fully) empty profile 
- files:
	- `.pdf` files with any leaked material
	- get the text/OCR it, gather most popular keywords and look for them later
	- reverse search images that appear there 
- code: 

https://en.wikipedia.org/wiki/Lists_of_currently_active_military_equipment_by_country

-----
### Platforms
##### GitHub
Framework for crawling - [`PyGithub`](https://github.com/PyGithub/PyGithub)
- Other libraries [recommended by GitHub](https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api?apiVersion=2022-11-28#python)
- [GitHub REST API docs](https://docs.github.com/en/rest/about-the-rest-api/about-the-rest-api?apiVersion=2022-11-28)

[What is a Web Crawler? And How Web Crawler works?](https://medium.datadriveninvestor.com/what-is-a-web-crawler-and-how-web-crawler-works-cbbd3983954f)
[Intro to `async` Python](https://www.youtube.com/watch?v=ftmdDlwMwwQ)

##### GitLab
Probably will look similar to GitHub, but I'm not entirely sure - never used it.
- [GitLab REST API docs](https://docs.gitlab.com/ee/api/rest/) 

##### Bitbucket
One way to search Bitbucket repos is by using `site:bitbucket.org` in Google (not sure if free ones have this hostname), but paid ones definitely can change the hostname, which is a problem.


----------------
### Leaks

Example military leaks:
https://www.reddit.com/r/OSINT/comments/12h318x/where_to_access_the_leaked_pentagon_documents/jftp6bm/
- https://disk . yandex.com/d/16vjq-DRn5YfUg
- https://drive . proton.me/urls/ERFZJ7ZGTM#aemsGZup78YU

Site with individuals records search - https://search.0t.rocks/
Something like `haveibeenpwned` - https://breachdirectory.org/
Another similar one - https://intelx.io/

[Tip: Don't pay for data leaks, they are free on BitTorrent DHT](https://www.reddit.com/r/OSINT/comments/ugep6q/tip_dont_pay_for_data_leaks_they_are_free_on/) 

	https://btdig.com

> Examples:
>[https://z.zz.fo/Oanja.png](https://z.zz.fo/Oanja.png)
[https://z.zz.fo/hye3Q.png](https://z.zz.fo/hye3Q.png)
[https://z.zz.fo/WkIIw.png](https://z.zz.fo/WkIIw.png)
[https://z.zz.fo/Kr0Xc.png](https://z.zz.fo/Kr0Xc.png)
These data dump collections can be found on DHT search engine like BTDig along with their magnets. All 4 magnets from screenshots above are live. Search with keywords like leak or website name. Use VM and use VPN.
Also this tool is for managing data breaches. [https://github.com/sensepost/Frack](https://github.com/sensepost/Frack)


![[Pasted image 20240104000109.png]]

[How to access Ransomware sites?](https://apexvicky.medium.com/how-to-access-ransomware-sites-1d0e96a31611)
[RaidForums leaked databases - insights and intelligence by KELA](https://www.kelacyber.com/unveiling-the-leaked-raidforums-database-insights-and-intelligence-by-kela/)

##### Other links

https://www.reddit.com/r/UkraineOSINT/
https://www.reddit.com/r/OSINTUkraine/
https://www.reddit.com/r/OSINT/comments/18wp8uh/research_ukraine/

Satellites - https://www.reddit.com/r/OSINT/comments/x8kzyf/best_commercial_satellite_companies_for_ukraine/

[CONFLICT IN UKRAINE, An example of Crowdsourcing-OSINT](https://www-brigadaosint-com.translate.goog/conflicto-en-ucrania-un-ejemplo-de-crowdsourcing-osint/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en)

https://www.bellingcat.com/ - the home of online investigations (also their discord)
https://www.projectowl.one/ - *Project Owl is the world's largest community for open-source intelligence.*
https://molfar.com/en/blog - *Molfar is the largest OSINT agency in Ukraine*
https://hackyourmom.com/en/category/kibervijna/speczialni-informaczijni-operacziyi/poshuk-ta-deanonimizacziya-vatnyka/ - another similar site

https://www.understandingwar.org/backgrounder/ukraine-conflict-updates - Ukraine conflict updates

https://www.reddit.com/r/opendirectories/ - subreddit with open directories and indexes found online 
[How To Find (Almost) Anything You Want On An Open Directory Page](https://www.reddit.com/r/opendirectories/comments/8zcbb/how_to_find_almost_anything_you_want_on_an_open/) - taken from `/r/opendirectories` wiki

https://osintukraine.com/ - 



-------------

#### Tools
https://github.com/lockfale/OSINT-Framework
https://osintframework.com/
https://github.com/danieldanielecki/IT-ARMY-of-Ukraine-Resources-in-English/tree/main
https://github.com/haris0/military-object
https://github.com/spatialillusions/TacticalJSON
https://www.google.com/search?q=github+military+#ip=1
https://www.google.com/search?q=russia+ukraine+war+open+source+mistakes+

google crawler using site:github.com,bitbucket.com,gitlab.com (or what the syntax is for multiple sites) \*phrase\*

##### Future reference 
https://sekurak.pl/prawdopodobnie-najwiekszy-cyberatak-w-historii-na-operatora-telekomunikacyjnego-uderzony-core-sieci-telekomunikacyjnej-najwiekszego-operatora-gsm-na-ukrainie/
- a cyberattack 

