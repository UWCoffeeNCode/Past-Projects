I have to preface this talk with: I am not a lawyer. This is intended as peer mentorship, not legal advice.

If you write something good, eventually someone may want to use it. It pays to think ahead a bit and ask yourself what you want them to use it for.

There's this "hacker" ethos that's common in programming. People want to make cool tools and they want others to use them. It's common for people to give away really valuable software – like Flask or Linux or Python for free.

And because such great free software exists, it's hard to get people to pay for a lot of software tools, unless you promise to make their life easier with them.

Everything you post to Github is by default copyright by you. It isn't patented – that's a separate legal process – but you still own the copyright for it and technically, you can sue people if they use it without permission.

Some sites have different models. Stack Overflow is CC-BY-SA for anything you write (like, in words) and MIT licensed for anything you post that's code. 

And if I do the job Ahrar has asked me to do well, you'll know what that means by the end of this talk.

CC-BY-SA is a Creative Commons license. These tend not to be used for programing – they're more for the arts. Plays, novels (like everything by Cory Doctorow) and photos are commonly released under one of the various Creative Commons licenses. Because it really isn't a single license, but a family of licenses.

I'm going to pause, very quickly, and explain why people use licenses at all. Wouldn't it be better to just explicitly specify what you want people to be able to do with your work each time?

There's a sense in which that's true, but it's also kind of a hassle and if there's one bet that always pays off, it's that people are lazy. These licenses I'm going to talk about are well known and have had actual lawyer input. That means they're probably more effective than whatever text you could throw together. That also means that people know how to use them and feel comfortable using them. Economists would say that there are low transaction costs to using them, which is why we see a few big licenses instead of many small ones.

Anyway, back to Creative Commons or CC. In order of increasing strictness, there is:

*	The CC-BY license, which just requires attribution. People can use your work for anything, as long as they credit you. By giving a work any CC license, you aren't renouncing copyright on a work, but you are saying that you won't sue anyone over it – that you're licensing absolutely anyone who wants to be licensed – as long as they stick to all of the other terms (like attribution) you add to the license.
*	CC-BY-SA, which requires attribution and anything created from the work to bear the same license
*	CC-BY-ND, which requires attribution and additionally, that if the work be shared, it be shared in its entirety and without modification.

(They all require attribution, by the way. The CC people found that no one ever used the version without attribution, so they decided to stop wasting their money on having lawyers update it)

*	CC-BY-NC, which requires attribution and forbids anyone from profiting from your work or a derivative work of it. 

You can add these together too. My blog is licensed under a CC-BY-NC-SA license. I want anyone to be able to draw from it, but I don't want them to be repackaging it and selling it (although honestly, if it was popular enough that people would do that, I'd be more happy than mad), I want credit, and I want derivative works to provide the same opportunities. 

The other license that I mentioned above is the MIT license. It's a very simple and short license. People can use anything that's MIT licensed for whatever they want, but they have to include the original copyright notice (which will have your name on it) even if it doesn't apply to the whole thing anymore (they'd have to append another license and explain which had jurisdiction where) and they cannot hold you responsible if your software does something horrible.

Most software licenses do this by the way. I'm not sure if there's really any risk to releasing code without a license that says "you can't sue me if something goes wrong", but lots of licenses will cover your bases here.

Then there's the GPL – GNU General Public License (GNU is an acronym too, sorry; it stands for GNU's not Unix and is the brainchild of Stallman. Their epic failure in their kernel project, Hurd, is why we have Linux today. Stallman is still salty about this and insists that it's called GNU-Linux, with GNU given precedence). 

The GPL has all the good stuff about not being legally responsible that the MIT license has. In addition, it explicitly requires all derivative works to in turn release their source code to anyone who is given binaries of them, or, in later versions, anyone given binaries or buying a product containing GPL licensed code. 

This came about because Stallman wrote a bunch of code at the MIT AI lab, then some of it was given to corporations, then they improved it and tried to sell binaries back to Stallman. And he was quite justifiably pissed off by this. 

The GPL embodies free as in freedom, not free as in free beer. Someone can still sell you GPL licensed code. They just have to give you the source code once they do and they can't stop you from sharing it with all your friends. 

It requires you to give the source code to hardware because of TiVo. TiVo claimed that even though they used GPL code in their device, they weren't giving compiled binaries per se, so they were exempt. There was a new version of the license to close this loophole, which is why you can download from the Samsung website all of the source code to every TV they produce that has GPL code in it – which I think is most of them because they use Linux under the hood.

It turns out it's cheaper and easier to just release their source code to the world then make a kernel from scratch.

You have to be careful of the GPL when providing compiled binaries (like video games) or hardware (like IoT devices) to people. It can "infect" code when used as libraries (this counts as using it) and then require the whole source code to be disclosed. This is why Microsoft is very careful to keep GPL licensed code out of Windows proper. It would require them to disclose their whole operating system code and obviously they really want to avoid this. 

If you are just providing a webapp, you only need to worry about the AGPL, but not the regular GPL. The AGPL expands the GPL to cover everything that uses GPL code and is served over the web. Because webapps – like Facebook -  don't provide binaries (although the Facebook mobile app and Facebook messenger do), they can safely use GPL licensed software with no disclosure requirements. I should also note that if you use a GPL licensed compiler, that's fine. It's just GPL licensed code being used _inside_ your code (again, even as libraries) that triggers the GPL.

The GPL is serious business and the GNU foundation will go to court to defend it. Courts have sided with them most of the time, too. It really is a valid license and it really can "infect" everything it touches. 

Of course, what's worrying when you're selling software is great when you're learning. The GPL means that there is a huge wealth of open source projects out there that you can look at and it's forced a lot of companies to open up the improvements they've made to those projects. Programmers as a group owe quite the debt to Richard Stallman for this unexpected bounty.

There's one last common family of license, which os the various copyleft licenses. These licenses have the liability limiting clauses that most software licenses do, paired with a sincere attempt to renounce all copyright (to the extent that the laws allow this). When laws don't, they grant unlimited license to use, copy, remix, etc. with no conditions. GitHib provides easy access to the Unlicense, which is pretty standard for the breed.

Github has really good support for licenses. It can walk you through picking a license and has simple English explanations of all of the major licenses. You can even see the license right on GitHub, highlighted in the top right of the code view, right next to the number of contributors. 

Licensed CC-BY-SA (C) 2018 Zachary Jacobi
