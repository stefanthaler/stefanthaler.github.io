---
title: Resources
permalink: /resources/
---

Here are some links, blogs, books and other things that I have found to be useful or interesting for myself. Perhaps they may also be useful for you.


## Some other good books
Some books that I strongly recommend to read.  For me, they have contained some valuable and often timeless lessons.
- [How to win friends and influence people](https://www.goodreads.com/book/show/4865.How_to_Win_Friends_and_Influence_People) by Dale Carnegie. This book contains practicable and timeless advice on how to improve the relationship to the people in your surroundings. The advice is often deceptively simple, but it seems that many people have forgotten or never learned even these simple things. Though many of the lessons in this book are fairly obvious if you think about it, it was an eye-opener for me in many ways. Highly recommended.
- [The ego is the enemy](https://www.goodreads.com/book/show/30370821-ego-is-the-enemy) by Ryan Holiday. In this book, Ryan Holiday brilliantly lays out how our own Ego betrays us and itself by preventing us from getting what Ego wants - success. I wish I had read this book earlier in my life, because I feel that some of my decisions where driven by my own ego without realizing it.  
- [If you want to write](https://www.goodreads.com/book/show/248954.If_You_Want_to_Write) by Brenda Ueland. For me, this book was a major contributor to unlocking my joy in writing. Read this if you want to write.
- [How to read a book](https://www.goodreads.com/book/show/567610.How_to_Read_a_Book) by Mortimer J. Adler. Reading seems to be such an obvious task that many people never consciously question what it actually means to read and how to become more proficient in it. This book taught me a whole lot about how to actually meaningfully read a book. In addition, by learning how to properly read it also increased my writing style.  
- [Presentation Zen](https://www.goodreads.com/book/show/1908456.Presentation_Zen) by Garr Reynolds. The core message that got stuck in my head from this book was: "Impress by clarity". That, and countless other tips and considerations on how to improve presentations. I wish many presenters in Academia had read this book, because I've seen quite some chaotic slides over the course of my time in Academia.
- [Atomic Habits](https://www.goodreads.com/book/show/40121378-atomic-habits) by James Clear. The best book about habit formation that I've read so. If you want to understand your habits, break bad ones or implement some good ones in your life then you should definitely have a look at this book. 

## Stuff I follow on the web
- [XKCD](https://xkcd.com/)
- [Explosm](http://explosm.net/)
- [Bruce Schneier's blog](https://schneier.com). To me, Bruce Schneier's blog is an excellent source for staying up to date with high-level developments in IT-security and privacy. To me, Bruce Schneier is also a role model on how to maintain a blog.
- [Graham Fuller's blog](http://grahamefuller.com/blog/). Graham Fuller is an ex-CIA Middle East expert, who critically comments on U.S. foreign policy every now and then.

## Inspiring Talks
- [How to write a great research paper](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) by Simon Peyton Jones. Probably the best talk on how to write a good paper. Caused a perspective shift in me, and helped me to appreciate the act of writing.
- [Why you should define your fears instead of your goals](https://www.ted.com/talks/tim_ferriss_why_you_should_define_your_fears_instead_of_your_goals]) by Tim Ferris. The major lesson that I drew from this talk was that I should consider the cost of inaction in any decision making. That is, what will it cost if don't change the status quo or don't act on something. This was a game changer on how I make decisions in my life.
<!--
You can see live demo [here](https://aweekj.github.io/Kiko-plus). This theme is inspired by [Kiko](http://github.com/gfjaru/Kiko) theme.

## Features

- Disqus comment system
- Google analytics
- Pagination support
- Custom tags
- SEO support


## Installation

#### Method 1: new master's repository (The Best)

1. First [fork](https://github.com/AWEEKJ/Kiko-plus/fork) it.
2. Change your forked repository name _Kiko-plus_ to __USERNAME.github.io__ where __USERNAME__ is your github username.
3. Access your new blog via [https://username.github.io](https://username.github.io).
4. [See configuration](#configuration).

#### Method 2: gh-pages in existing repository

1. Create a new branch called _gh-pages_ in the repository where you want to add a template [managing branches](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/).
2. From command line run `git clone https://github.com/AWEEKJ/Kiko-plus.git` - this will clone _Kiko-plus_ template to your computer.
3. Create new branch `git checkout -b gh-pages` where _gh-pages_ will be your branch name.
4. Add remote, which is your repo from the first step, to your new branch `git remote add gh-pages https://github.com/<yourName>/<yourMaster>/gh-pages`. _yourName_ is your account name and _yourMaster_ is your repository.
5. Push new branch to remote `git push gh-pages`.
6. Update `_config.yml` file by changing `baseurl: "<branchName>"` _branchName_ is your branch name where _gh-pages_ resides. See [configuration](#configuration).

#### Method 3: Run it locally

1. Download [zip](https://github.com/AWEEKJ/Kiko-plus/archive/master.zip) or clone it `git clone https://github.com/AWEEKJ/Kiko-plus`.
2. Go inside folder and run `jekyll serve` or `rake preview`. This will build a website which you can access [https://localhost:4000](https://localhost:4000). You need to have [Jekyll](https://jekyllrb.com/docs/installation/) installed to do this.


## Configuration

All configuration is done via `_config.yml` file which you will find in your main repo folder. Change this `<something>` to yours.

### Basic

- Config your blog name.

```yml
name: <blog-name>
```

- These configuration in `author:` is for links to icons in footer. If you want to add more link icons, modify `_includes/footer.html` file.

```yml
author:
  facebook:         your-id
  twitter:          your-id
  github:           your-id
  linkedin:         your-id
  medium:           your-id
  tumblr:           your-id
  email:            your-id@your-email.com
```

- Change copyright year and name in footer.

```yml
copyright:
  year:             2017
  name:             Kiko
```

### Google analytics

- Change this to your Google Analytic ID.

```yml
google-analytics:
  id:               "your-id"
```

### Disqus

- Change this to your Disqus short name.

```yml
disqus:
  id:               "your-id"
```

### URL

- Config your domain.

```yml
url: "https://<your-name>.github.io"
```

- **NOTE** When if running locally, change url to

```yml
url: "https://localhost:4000"
```

- Change this to your branch name where _gh-pages_ resides.
- **NOTE** apply only if you used __Method 2__ for installation.

```yml
baseurl: "/<branch-name>"
```

## Rakefile Usage

```bash
# Create new post
$ rake post title="A Title" [date="2015-08-16"] [tags="[tag1, tag2]"]

# Create new draft post
$ rake draft title="A Title" [date="2015-08-16"] [tags="[tag1, tag2]"]

# Install Jekyll Plugins. Do before running in local.
$ rake geminstall

# Run in Local
$ rake preview
```

## License

This theme is released under MIT License.
-->
