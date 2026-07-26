<p align="center">
  <img src="./assets/header.png" width="100%" alt="İhsan Deniz — local-first AI tools">
</p>

<p align="center">
  <a href="https://github.com/ihsandeniz">
    <img
      src="https://github-readme-activity-graph.vercel.app/graph?username=ihsandeniz&amp;bg_color=00000000&amp;color=8b98a8&amp;title_color=8b98a8&amp;line=22d3ee&amp;point=f2cc60&amp;area_color=22d3ee&amp;area=true&amp;hide_border=true&amp;grid=false&amp;height=300&amp;days=31&amp;custom_title=Contribution%20activity%20%C2%B7%20last%2031%20days"
      width="100%"
      alt="İhsan Deniz contribution activity over the last 31 days"
    >
  </a>
</p>

<p align="center">
  <a href="https://ihsandeniz.net.tr"><b>ihsandeniz.net.tr</b></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://x.com/idkgen0"><b>X / @idkgen0</b></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://www.threads.net/@idkgen0"><b>Threads / @idkgen0</b></a>
</p>

<br>

## What I am building now

<table>
  <tr>
    <td valign="top">
      <sub>FLAGSHIP / IN ACTIVE DEVELOPMENT</sub>
      <h2><a href="https://ihsandeniz.net.tr/proje.html?p=alice">Alice AI — Yuki</a></h2>
      <p><strong>A voice AI companion that lives on your machine, not on someone's server.</strong></p>
      <p>
        Most AI companions are a browser tab in front of infrastructure you do not control:
        the conversations sit in someone else's database, the voice is rented, and the whole
        thing stops existing the day the service does.
      </p>
      <p>
        Yuki is a desktop app. Speech recognition runs on your own CPU (faster-whisper),
        long-term memory is a vector store on your own disk, and the model is whichever one you
        bring a key for — OpenRouter, OpenAI, Gemini, or a local Ollama. It ships with a large set of system
        tools: screen capture, files, shell, web search and browsing, clipboard, media and window
        control, notifications, memory search.
      </p>
      <p>
        Two faces: a classic chat window, and <strong>HALKA</strong> — a ring HUD that sits on the desktop.
      </p>
      <p>
        <strong>The free Lite build is out for Linux</strong> (AppImage, no installation).
        The paid tiers — persistent long-term memory and offline licensing — are built;
        the commercial launch is still pending.
      </p>
      <p>
        <a href="https://ihsandeniz.net.tr/proje.html?p=alice"><b>project page</b></a>
        &nbsp;&nbsp;·&nbsp;&nbsp;
        <a href="https://github.com/ihsandeniz/yuki-ai/releases/latest"><b>download Yuki Lite</b></a>
      </p>
    </td>
  </tr>
</table>

<br>

<table>
  <tr>
    <td width="66%" valign="middle">
      <h2>One person. No company, no team.</h2>
      <p>
        Architecture, code, design, docs, deployment — all of it is me. I ship in public and I try
        not to announce anything I have not actually run. Where a project is unfinished, the README
        says so.
      </p>
      <p>
        The common thread across everything here: <strong>it runs on hardware you own.</strong>
        No account to create, no telemetry, and no service of mine sitting between you and your
        own data. You bring the key; the files stay where they are.
      </p>
      <p>
        <code>PYTHON</code>&nbsp;
        <code>FASTAPI</code>&nbsp;
        <code>TYPESCRIPT</code>&nbsp;
        <code>VANILLA&nbsp;JS</code>&nbsp;
        <code>POSTGRES · PGVECTOR</code>&nbsp;
        <code>ARCH&nbsp;LINUX</code>
      </p>
    </td>
    <td width="34%" align="center" valign="middle">
      <img src="./assets/mark.png" width="170" alt="HALKA — the ring HUD mark">
      <br>
      <sub><b>HALKA</b> · the ring</sub>
    </td>
  </tr>
</table>

<br>

## Open source

> Every one of these is a tool I use myself. Self-hosted, bring-your-own-key, no cloud account.

| Project | What it is |
| --- | --- |
| **[usage&#8209;tracker](https://github.com/ihsandeniz/usage-tracker)** <br> <sub>Python · MIT</sub> | A *Pane for Linux*: all your AI usage, rate limits and real dollar spend in one place — a waybar badge, a floating widget, or a web panel. Guided setup that shows you every line before it writes it, and undoes it from the same screen. stdlib Python + Vanilla JS, zero dependencies, loopback-only. |
| **[galleryweb](https://github.com/ihsandeniz/galleryweb)** <br> <sub>Python · AGPL-3.0</sub> | A self-hostable photo & video gallery with a real editing studio — crop, rotate, filters, colour and light adjustment, video trimming. No login, no cloud account: double-click and it runs. FastAPI + Vanilla JS. |
| **[uai&#8209;agents](https://github.com/ihsandeniz/uai-agents)** <br> <sub>TypeScript · MIT</sub> | A six-agent autonomous orchestration system you run on your own server. A router analyses each task, hands it to the right specialist, and a QA agent checks the result; past runs are embedded into pgvector so routing improves over time. In-process event bus, no external queue. |
| **[yuki&#8209;ai](https://github.com/ihsandeniz/yuki-ai)** | Release channel for the free Yuki Lite build — a single AppImage, nothing to install. |

<br>

<p align="center">
  <img src="./assets/footer.png" width="100%" alt="No telemetry. No account. It runs on hardware you own.">
</p>

<p align="center">
  <sub>Header art generated from <a href="./build">./build</a> — plain HTML, rendered locally. No external services.</sub>
</p>
