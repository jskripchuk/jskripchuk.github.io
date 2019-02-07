---
layout: post
title: Collaborate on Code and Content with Atom-Teletype and Git
date: 2018-12-17
overlay: purple
hero: 'https://upload.wikimedia.org/wikipedia/commons/0/0a/What-is-teletype.jpg'
cover_cite: 'Cover image via [Wikimedia](https://commons.wikimedia.org/wiki/File:What-is-teletype.jpg)'
tags:
- atom
- collaboration
- git
- teletype
---

<i class="fas fa-atom"></i> [Atom](https://atom.io/) is my go-to text editor. It's open source, slick, maintained by GitHub, and has a ton of [community-contributed packages](https://atom.io/packages) available so you can to mould it to fit your needs. I use packages for [writing and previewing markdown](https://atom.io/packages/markdown-preview), [linting code](https://atom.io/packages/linter), [checking my spelling](https://atom.io/packages/spell-check) and [more](https://atom.io/packages/atomify) pretty much every day.

The newest package I've been using is [Teletype](https://teletype.atom.io/), which lets you collaborate on files locally via real-time peer-to-peer 'portals' in Atom.


<video src='https://teletype.atom.io/videos/real-time.mp4' type='video/mp4' style='width:100%;' height='450' autoplay loop muted></video>
<sup class='caption' style='margin-top:-10px;'>Video via <a href="https://atom.io">Atom.io</a></sup>

If you have a GitHub account, you can generate a token for creating and joining portals. Participants can then collaborate synchronously on files just like they do in Google Docs, only better: Atom enforces UTF-8 encoding and it formats code according to best practices, so you won't need to separate your content editing workflow from your code contribution workflow.

Atom-teletype can also help you avoid unnecessary git merge conflicts when collaborating rapidly during hackathons and sprints. This makes it a great option for classrooms: it lets contributors leverage Git for version control and collaboration without the full weight of [developer operations](https://en.wikipedia.org/wiki/DevOps) overhead. An admin or content editor can commit collaborative changes the project GitHub repository on an ongoing, basis making it possible for students to contribute without needing write-access to the repository itself. Portals are file-specific, so security risks and accidental changes are minimized.

## Caveat

It's important to note that Teletype is in Beta, so it's still a bit buggy! For short, one-off workshops, it might not be worth the effort to troubleshoot it quite yet.
