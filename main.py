





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-hddDYPWR0gBbqLRmIZP242WMEiYsVkYI2UCYCVUHB4h5DhD2cbtFJYG+HPh21dZGb+sbgDHxQBNJCBq7YbmlBQ==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-02a3eaa24db2bd1ed9b64450595fc2cf.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-Fr8GYcjC9Pwm6dQmefd4vXX2fXl7gylXrhSo2aMCxM0Ilrme82PXVtfHOzcnvR9vUmfvO8t8XVmNxW1FRnoYSg==" rel="stylesheet" href="https://github.githubassets.com/assets/github-8f8f40cebc9aea61f6dac776b58ccad9.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>Text-Editor/main.py at master · amandeep511997/Text-Editor</title>
    <meta name="description" content="A rich text editor implemented in Python using Tkinter - amandeep511997/Text-Editor">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars0.githubusercontent.com/u/19922632?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="amandeep511997/Text-Editor" /><meta name="twitter:description" content="A rich text editor implemented in Python using Tkinter - amandeep511997/Text-Editor" />
    <meta property="og:image" content="https://avatars0.githubusercontent.com/u/19922632?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="amandeep511997/Text-Editor" /><meta property="og:url" content="https://github.com/amandeep511997/Text-Editor" /><meta property="og:description" content="A rich text editor implemented in Python using Tkinter - amandeep511997/Text-Editor" />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NDgzMzk2NDQ2OmI2YWM0MjJkZjU2ZDExNTI2YWJiOWEzOGRkZDgyNzMzMTFiNzMyZWEwM2I2NzU2Y2QxY2FkMWY4OGI5MGVmNzk=--1de6eedb1b352bc2ad4887da4fecead4a50a4abf">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="request-id" content="8398:290C:9D365D:EB7997:5E0BC10F" data-pjax-transient>



  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

    <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="8398:290C:9D365D:EB7997:5E0BC10F" /><meta name="octolytics-dimension-region_edge" content="ap-south-1" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-dimension-visitor_id" content="8229980621510501855" /><meta name="octolytics-actor-id" content="55187704" /><meta name="octolytics-actor-login" content="dk-dinesh" /><meta name="octolytics-actor-hash" content="672d32b2292087731d22e37f2aca9ba30b27b69505e58173cfaefc34816f357e" />

<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="193f8b6954cd103f5a25d22c6c65528c">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="dk-dinesh">

      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="ZmI5NmYyYjE3YWU4NDYzMTFjZDI3OTQwYzk2MmJkYmU2MGNlNDAxNDJmNzQ5ZTQ5YmU4YTJkYTQxYTIwOWRjNnx7InJlbW90ZV9hZGRyZXNzIjoiMTM5LjE2Ny4yMTYuMTM4IiwicmVxdWVzdF9pZCI6IjgzOTg6MjkwQzo5RDM2NUQ6RUI3OTk3OjVFMEJDMTBGIiwidGltZXN0YW1wIjoxNTc3ODI4NjM0LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS,NOTIFY_ON_BLOCK,RELATED_ISSUES,GHE_CLOUD_TRIAL">

    <meta name="html-safe-nonce" content="1e71132396d59dbb1845e817ada776dd84e5af10">

  <meta http-equiv="x-pjax-version" content="88749827de37e0e1ebd70bc0919cebf3">
  

      <link href="https://github.com/amandeep511997/Text-Editor/commits/master.atom" rel="alternate" title="Recent Commits to Text-Editor:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/amandeep511997/Text-Editor git https://github.com/amandeep511997/Text-Editor.git">

  <meta name="octolytics-dimension-user_id" content="19922632" /><meta name="octolytics-dimension-user_login" content="amandeep511997" /><meta name="octolytics-dimension-repository_id" content="116910473" /><meta name="octolytics-dimension-repository_nwo" content="amandeep511997/Text-Editor" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="116910473" /><meta name="octolytics-dimension-repository_network_root_nwo" content="amandeep511997/Text-Editor" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/amandeep511997/Text-Editor/blob/master/main.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <meta name="webauthn-auth-enabled" content="true">

  <meta name="webauthn-registration-enabled" content="true">

  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
      <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
    </span>

    
    
    


          <header class="Header js-details-container Details flex-wrap flex-lg-nowrap p-responsive" role="banner">

    <div class="Header-item d-none d-lg-flex">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

    </div>

    <div class="Header-item d-lg-none">
      <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
        <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
      </button>
    </div>

    <div class="Header-item Header-item--full flex-column flex-lg-row width-full flex-order-2 flex-lg-order-none mr-0 mr-lg-3 mt-3 mt-lg-0 Details-content--hidden">
        <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="116910473" data-scoped-search-url="/amandeep511997/Text-Editor/search" data-unscoped-search-url="/search" action="/amandeep511997/Text-Editor/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=miynWnYhRBc79kMk1a+N571nZ8Bu9hERkorDJbl3H+HNRNz1jfTlGXPVZcEU+NqbuCDTUoyKerWpl1Pxp6uKMQ=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


      <nav class="d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto" aria-label="Global">
    <a class="Header-link d-block d-lg-none py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>
  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>
    <div class="mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-lg-none mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" href="https://github.com/dk-dinesh">
      <img class="avatar" height="20" width="20" alt="@dk-dinesh" src="https://avatars3.githubusercontent.com/u/55187704?s=60&amp;v=4" />
      dk-dinesh
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="+vz5cyXWEWdxRLxskLq0qMsOSpS4Kjxl/xqLb2h8WENhdUTz/46zzA1DHr/bC0PhH3dzsS/0FGJop7N46J/sCA==" />
      <button type="submit" class="Header-link mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15 d-lg-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9V7H8V5h4V3l4 3-4 3zm-2 3H6V3L2 1h8v3h1V1c0-.55-.45-1-1-1H1C.45 0 0 .45 0 1v11.38c0 .39.22.73.55.91L6 16.01V13h4c.55 0 1-.45 1-1V8h-1v4z"/></svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-lg-none position-relative">
      <div class="css-truncate css-truncate-target width-fit position-absolute left-0 right-0 text-center">
              <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <a class="Header-link" href="/amandeep511997">amandeep511997</a>
    /
    <a class="Header-link" href="/amandeep511997/Text-Editor">Text-Editor</a>

</div>
    </div>


    <div class="Header-item mr-0 mr-lg-3 flex-order-1 flex-lg-order-none">
      

    <a aria-label="You have no unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:55187704" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </div>


    <div class="Header-item position-relative d-none d-lg-flex">
      <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="amandeep511997/Text-Editor">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/amandeep511997/Text-Editor/issues/new" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-lg-flex">
      
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/dk-dinesh/feature_preview/indicator_check.json">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img alt="@dk-dinesh" class="avatar" src="https://avatars0.githubusercontent.com/u/55187704?s=40&amp;v=4" height="20" width="20">
      <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-2" style="width: 180px">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/dk-dinesh" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">dk-dinesh</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:19922632,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:55187704,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;}}" data-hydro-click-hmac="b8f0f5e66432b4ded2595afeda5d02cce1ba59c9af327445ffcfc31c91c28a78">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
"
            style="max-width: 29px"
          >
          <div class="user-status-emoji-container flex-shrink-0 mr-1 mt-1 lh-condensed-ultra v-align-bottom" style="">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6"
           style="line-height: 20px;" >
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
              <span class="text-gray ml-2">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="iAbAVxO1fYj0B7BYI5Hn5e30FOM52vTE6z+PFDIKC4IWOJXzpDf+HdBAFwLU0wIlaudg3QgEX5no/ncOMF2diw==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value=""
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
            

<div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-01-01T03:43:54+05:30">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-01-01T04:13:54+05:30">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-01-01T07:13:54+05:30">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-01-01T23:59:59+05:30">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-01-05T23:59:59+05:30">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>


    <a role="menuitem" class="dropdown-item" href="/dk-dinesh" data-ga-click="Header, go to profile, text:your profile">Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/dk-dinesh?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

    <a role="menuitem" class="dropdown-item" href="/dk-dinesh?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="/dk-dinesh?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/dk-dinesh/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}"
    data-feature-preview-close-hmac="ecf42179fac900577d39ff7a51f64b7c48074af3680105a5550d6fddcbcd8ee6"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}"
    data-hydro-click-hmac="c51b5516ee3aaa6eb372eb5147d96bdb76945268b97f70052d58fbf2967aef8e"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="P+dqaQOFC2XlAGlFMu12wj7e48ly/kbLJr4GFc4y6GGkbtfp2d2pzpkHy5Z5XIGL6qfa7OUgbsyxAz4CTtFcKg==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_abd2" hidden="hidden" class="form-control" />
<input type="hidden" name="timestamp" value="1577828634703" class="form-control" />
<input type="hidden" name="timestamp_secret" value="5b5923c5ae730213fb19e52e447302bfe35b89e0171403f008e2caba82beb09b" class="form-control" />

</form>  </details-menu>
</details>

    </div>

  </header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      


  

      <div class="border-bottom shelf intro-shelf js-notice mb-0 pb-4">
  <div class="width-full container">
    <div class="width-full mx-auto shelf-content">
      <h2 class="shelf-title">Learn Git and GitHub without any code!</h2>
      <p class="shelf-lead">
          Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
      </p>
      <a class="btn btn-primary shelf-cta" target="_blank" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;READ_GUIDE&quot;,&quot;repository_id&quot;:116910473,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="1d1de80f97527ec636498ba0438938795b827fbda5c782049e86663eb3aef5a2" href="https://guides.github.com/activities/hello-world/">Read the guide</a>
    </div>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="shelf-dismiss js-notice-dismiss" action="/dashboard/dismiss_bootcamp" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="4yaqFawTbW4D6uGSE6Qa3ZSXTBbH6pr2XDZwZgQfA6y4joSeZAvaOPWwa5Q4EfFIdd/yVaeCs38JJsCcxdzN4A==" />
      <button name="button" type="submit" class="mr-1 close-button tooltipped tooltipped-w" aria-label="Hide this notice forever" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;DISMISS_BANNER&quot;,&quot;repository_id&quot;:116910473,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="6c61596ded38fd6996afb97251042fef999a47d79d9ebdf6a31537a3cfc03b7f">
        <svg aria-label="Hide this notice forever" class="octicon octicon-x v-align-text-top" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
</button></form>  </div>
</div>










  <div class=" pagehead repohead readability-menu experiment-repo-nav pt-0 pt-lg-4 ">
    <div class="repohead-details-container clearfix container-lg p-responsive d-none d-lg-block">

      <ul class="pagehead-actions">




  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="clearfix js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="uiIhauzEJDBuKUm2+CwPWqmZ7TpCrXz8e/0R5ex/AXeW+GCAJws1Cw8OYV3B048MmymRFr2eZXPZH9UjWaSrFA==" />      <input type="hidden" name="repository_id" value="116910473">

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:116910473,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="66b68da8a7be62c752b4d48344850f37b1b2ce21b48ff989392e6dec47c858cb" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Watch
          </span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/amandeep511997/Text-Editor/watchers"
          aria-label="1 user is watching this repository">
          1
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/amandeep511997/Text-Editor/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="5R5r6Fy4WlKecSWx+tHIEyfiXPUIa+8T10ArTACBePH7fPdJxgohj2lrClhtuhbRwqYsFHjXhljcVRZXhMq2KQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar amandeep511997/Text-Editor" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:116910473,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="04405a190bf23df62a467f7e98d97cf6806cfb015b46dd296e19134f0025f3a9" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg aria-label="star" height="16" class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" role="img"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>

        Unstar
</button>        <a class="social-count js-social-count" href="/amandeep511997/Text-Editor/stargazers"
           aria-label="7 users starred this repository">
           7
        </a>
</form>
    <form class="unstarred js-social-form" action="/amandeep511997/Text-Editor/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="NBCvHrqKqrP/LtnXHLj5dEfBszw3mk1bwXa/xhOQ3sM8yUNzwaWjPCFr0W8SA5enipVuf00EEi0tYYfK28Sv+g==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star amandeep511997/Text-Editor" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:116910473,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="04af0975b5b24d973dd3f5510c7375e2fc80ce5855daca0b7d80872b489c7a3e" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg aria-label="star" height="16" class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" role="img"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>

        Star
</button>        <a class="social-count js-social-count" href="/amandeep511997/Text-Editor/stargazers"
           aria-label="7 users starred this repository">
          7
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/amandeep511997/Text-Editor/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="yc3XQaT/wmOHEFx/HCvm+ayISfNtGgXq9Q8BlUrk6+F3HTy5IBBhhzQVMOc4YFSomNQGRUDf+fLk94YV3N8P6Q==" />
            <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:116910473,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="14563444d2d2fbdc27776668a94f1965fab4808d90c2b2f246d842deed795ef7" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of amandeep511997/Text-Editor to your account" aria-label="Fork your own copy of amandeep511997/Text-Editor to your account">              <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 00-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 002 1a1.993 1.993 0 00-1 3.72V6.5l3 3v1.78A1.993 1.993 0 005 15a1.993 1.993 0 001-3.72V9.5l3-3V4.72A1.993 1.993 0 008 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
</button></form>
    <a href="/amandeep511997/Text-Editor/network/members" class="social-count"
       aria-label="6 users forked this repository">
      6
    </a>
  </li>
</ul>

      <h1 class="public ">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/amandeep511997/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/amandeep511997">amandeep511997</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/amandeep511997/Text-Editor">Text-Editor</a></strong>
  

</h1>

    </div>
    
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /amandeep511997/Text-Editor" href="/amandeep511997/Text-Editor">
      <div class="d-inline"><svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg></div>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /amandeep511997/Text-Editor/issues" href="/amandeep511997/Text-Editor/issues">
        <div class="d-inline"><svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 011.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg></div>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" data-skip-pjax="true" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /amandeep511997/Text-Editor/pulls" href="/amandeep511997/Text-Editor/pulls">
      <div class="d-inline"><svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg></div>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="4">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement" class="position-relative float-left">
      <a data-hotkey="g w" data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /amandeep511997/Text-Editor/actions" href="/amandeep511997/Text-Editor/actions">
        <div class="d-inline"><svg class="octicon octicon-play" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8A7 7 0 110 8a7 7 0 0114 0zm-8.223 3.482l4.599-3.066a.5.5 0 000-.832L5.777 4.518A.5.5 0 005 4.934v6.132a.5.5 0 00.777.416z"/></svg></div>
        Actions
</a>
    </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /amandeep511997/Text-Editor/projects" href="/amandeep511997/Text-Editor/projects">
      <div class="d-inline"><svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg></div>
      Projects
      <span class="Counter" >0</span>
</a>

    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /amandeep511997/Text-Editor/wiki" href="/amandeep511997/Text-Editor/wiki">
      <div class="d-inline"><svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg></div>
      Wiki
</a>
    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /amandeep511997/Text-Editor/security/advisories" href="/amandeep511997/Text-Editor/security/advisories">
      <div class="d-inline"><svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg></div>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /amandeep511997/Text-Editor/pulse" href="/amandeep511997/Text-Editor/pulse">
      <div class="d-inline"><svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg></div>
      Insights
</a>

</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /amandeep511997/Text-Editor" href="/amandeep511997/Text-Editor">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /amandeep511997/Text-Editor/issues" href="/amandeep511997/Text-Editor/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /amandeep511997/Text-Editor/pulls" href="/amandeep511997/Text-Editor/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /amandeep511997/Text-Editor/projects" href="/amandeep511997/Text-Editor/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_wiki /amandeep511997/Text-Editor/wiki" href="/amandeep511997/Text-Editor/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /amandeep511997/Text-Editor/security/advisories" href="/amandeep511997/Text-Editor/security/advisories">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="6">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /amandeep511997/Text-Editor/pulse" href="/amandeep511997/Text-Editor/pulse">
        Pulse
</a>
      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="community /amandeep511997/Text-Editor/community" href="/amandeep511997/Text-Editor/community">
          Community
</a>      </span>

  </nav>
</div>


  </div>
<div class="container-lg clearfix new-discussion-timeline experiment-repo-nav  p-responsive">
  <div class="repository-content ">

    
    


  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/amandeep511997/Text-Editor/blob/8ef6bc2aa5c315d798630e6cd8835087284756c6/main.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:7ada0dcff1f0a0708f34c32bfce379f5 -->
      

    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-column flex-md-row">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay select-menu branch-select-menu  hx_rsm" id="branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>master</span>
  </summary>

  <details-menu class="select-menu-modal hx_rsm-modal position-absolute" style="z-index: 99;" src="/amandeep511997/Text-Editor/refs/master/main.py?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/amandeep511997/Text-Editor/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="main.py" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/amandeep511997/Text-Editor"><span>Text-Editor</span></a></span></span><span class="separator">/</span><strong class="final-path">main.py</strong>
          <span class="separator">/</span>
          
<details class="details-reset details-overlay select-menu d-inline">
  <summary class="btn-link link-gray select-menu-button css-truncate" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="ae4fb30f2fca46b8244452550157049717ab3cf0297b950a0b184cbd674ea776">
    <span data-menu-button>Jump to</span>
  </summary>
  <details-menu class="select-menu-modal position-absolute" style="z-index: 99;">
    <div class="select-menu-header">
      <span class="select-menu-title">Code definitions</span>
    </div>
    <div class="select-menu-filters">
      <div class="select-menu-text-filter">
        <input
          type="text"
          id="code-def-filter-field"
          class="form-control js-filterable-field"
          placeholder="Filter definitions"
          aria-label="Filter definitions"
          autofocus
          autocomplete="off">
      </div>
    </div>
    <div class="select-menu-list lh-default" data-filterable-for="code-def-filter-field" data-filterable-type="substring">
      
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L35">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    make_tag
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L64">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    new
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L71">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    open_file
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L78">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    save
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L87">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    save_as
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L100">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    rename
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L116">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    close
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L122">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    cut
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L130">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    copy
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L137">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    paste
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L142">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    delete
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L145">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    undo
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L148">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    redo
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L151">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    select_all
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L154">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    delete_all
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L159">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    change_color
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L175">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    check
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L190">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    find_text
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L203">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    find_text_cancel_button
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L210">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    bold
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L220">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    italic
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L229">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    underline
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L237">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    strike
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L247">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    highlight
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L261">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    remove_align_tags
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L271">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    align_center
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L277">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    align_justify
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L281">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    align_left
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L287">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    align_right
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L296">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    change_font
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L302">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    change_size
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L543">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    about
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L606">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    on_enter
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}" data-hydro-click-hmac="32640dbac47ce2897ece1dede6a9355a5a206938c8c2ef91b7c2d3d7a5558313" href="/amandeep511997/Text-Editor/blob/master/main.py#L610">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    on_leave
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
    </div>
  </details-menu>
</details>

      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/amandeep511997/Text-Editor/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="main.py" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>

    



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/users/amandeep511997/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/amandeep511997"><img class="avatar" src="https://avatars1.githubusercontent.com/u/19922632?s=40&amp;v=4" width="20" height="20" alt="@amandeep511997" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="author" data-hovercard-type="user" data-hovercard-url="/users/amandeep511997/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/amandeep511997">amandeep511997</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="First commit" class="link-gray" href="/amandeep511997/Text-Editor/commit/9a2d4d7dd70c2e6cae5d78effc18928be9296425">First commit</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/amandeep511997/Text-Editor/commit/9a2d4d7dd70c2e6cae5d78effc18928be9296425" data-pjax>9a2d4d7</a>
          <relative-time datetime="2018-01-10T05:01:37Z" class="no-wrap">Jan 10, 2018</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link">
          <span><strong>1</strong> contributor</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/amandeep511997/Text-Editor/contributors-list/master/main.py" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
    </div>
  </div>





    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      675 lines (540 sloc)
      <span class="file-info-divider"></span>
    23.6 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/amandeep511997/Text-Editor/raw/master/main.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/amandeep511997/Text-Editor/blame/master/main.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/amandeep511997/Text-Editor/commits/master/main.py">History</a>
    </div>


    <div>

            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/amandeep511997/Text-Editor/edit/master/main.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="dIpaLVyQd/MKSHJGiHgbTMnr8zns0n28SdAgZ6t5+8RKcLAA5OcmUr4hBqxEEzZC3axEHjxReZCzR8jmmDMSAQ==" />
              <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
                aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
                <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 011.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
              </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/amandeep511997/Text-Editor/delete/master/main.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="3elG/ZiOK/203Ynkd7PagXcwW4wZBbkK4Fb/CSymwyNuEWqVYKDxKP/4vuli3FQQ9wx5UYyCuL1I3Iqxzl6GPg==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
            </button>
</form>    </div>
  </div>
</div>



        <div class="f6 v-align-middle text-gray px-3 py-2 border-bottom bg-gray-light d-flex flex-justify-between">
            <div class="d-flex text-mono">
              <svg style="color: #28a745;" class="octicon octicon-primitive-dot mr-2" viewBox="0 0 8 16" version="1.1" width="8" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 8c0-2.2 1.8-4 4-4s4 1.8 4 4-1.8 4-4 4-4-1.8-4-4z"/></svg>
              <span>You're using code navigation to jump to definitions or references.</span>
            </div>
            <div>
              <a href="https://help.github.com/en/articles/navigating-code-on-github">Learn more</a>
              or
              <a href="mailto:code-nav@github.com">give us feedback</a>
            </div>
        </div>

      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/python2</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> Tkinter <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkFileDialog <span class="pl-k">as</span> filedialog <span class="pl-c"><span class="pl-c">#</span> filedialog allows user to select where they want to save the file.</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkFont</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkColorChooser <span class="pl-k">as</span> colorchooser</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> ttk</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkSimpleDialog <span class="pl-k">as</span> simpledialog</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkMessageBox <span class="pl-k">as</span> messagebox</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">PIL</span> <span class="pl-k">import</span> Image, ImageTk</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkMessageBox <span class="pl-k">as</span> messagebox</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tkFileDialog <span class="pl-k">import</span> askopenfilename</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> creating the root of the window.</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">master <span class="pl-k">=</span> Tk()</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">master.title(<span class="pl-s"><span class="pl-pds">&quot;</span>Untitled* - Script Editor<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">master.geometry(<span class="pl-s"><span class="pl-pds">&quot;</span>600x550<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> setting resizable window</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">master.resizable(<span class="pl-c1">True</span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">master.minsize(<span class="pl-c1">600</span>, <span class="pl-c1">550</span>) <span class="pl-c"><span class="pl-c">#</span> minimimum size possible</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> --------------- METHODS ---------------- #</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> MAIN MENU METHODS </span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">file_name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span> <span class="pl-c"><span class="pl-c">#</span> Current file name.</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">current_font_family <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Liberation Mono<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">current_font_size <span class="pl-k">=</span> <span class="pl-c1">12</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">fontColor <span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>#000000<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">fontBackground<span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#FFFFFF<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">make_tag</span>():</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">		weight <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">		weight <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>normal<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>italic<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">		slant <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>italic<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">		slant <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>roman<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>underline<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">		underline <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">		underline <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>overstrike<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">		overstrike <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">		overstrike <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">	big_font <span class="pl-k">=</span> tkFont.Font(text, text.cget(<span class="pl-s"><span class="pl-pds">&quot;</span>font<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">	big_font.configure(<span class="pl-v">slant</span><span class="pl-k">=</span> slant , <span class="pl-v">weight</span><span class="pl-k">=</span> weight , <span class="pl-v">underline</span><span class="pl-k">=</span> underline , <span class="pl-v">overstrike</span><span class="pl-k">=</span> overstrike , <span class="pl-v">family</span><span class="pl-k">=</span> current_font_family , <span class="pl-v">size</span><span class="pl-k">=</span> current_font_size )</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">	text.tag_config(<span class="pl-s"><span class="pl-pds">&quot;</span>BigTag<span class="pl-pds">&quot;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>big_font , <span class="pl-v">foreground</span><span class="pl-k">=</span> fontColor , <span class="pl-v">background</span><span class="pl-k">=</span> fontBackground) </td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>BigTag<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span>  current_tags:</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">		text.tag_remove(<span class="pl-s"><span class="pl-pds">&quot;</span>BigTag<span class="pl-pds">&quot;</span></span> , <span class="pl-c1">1.0</span> , <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">	text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>BigTag<span class="pl-pds">&quot;</span></span> , <span class="pl-c1">1.0</span> , <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">new</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">	file_name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">	ans <span class="pl-k">=</span> messagebox.askquestion(<span class="pl-v">title</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Save File<span class="pl-pds">&quot;</span></span> , <span class="pl-v">message</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Would you like to save this file<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> ans <span class="pl-k">is</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">		save()</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">	delete_all()</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">open_file</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">	new()</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">	<span class="pl-v">file</span> <span class="pl-k">=</span> filedialog.askopenfile()</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> file_name</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">	file_name <span class="pl-k">=</span> <span class="pl-v">file</span>.name</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">	text.insert(<span class="pl-c1">INSERT</span> , <span class="pl-v">file</span>.read())</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">save</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> file_name</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> file_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">		path <span class="pl-k">=</span> filedialog.asksaveasfilename()</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">		file_name <span class="pl-k">=</span> path</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">	master.title(file_name <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - Script Editor<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">	write <span class="pl-k">=</span> <span class="pl-c1">open</span>(file_name, <span class="pl-v">mode</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">	write.write(text.get(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>))</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">save_as</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> file_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">		save()</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span>break<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">	f <span class="pl-k">=</span> filedialog.asksaveasfile(<span class="pl-v">mode</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    	<span class="pl-k">if</span> f <span class="pl-k">is</span> <span class="pl-c1">None</span>: </td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        	<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    	text2save <span class="pl-k">=</span> <span class="pl-c1">str</span>(text.get(<span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)) </td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    	f.write(text2save)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    	f.close() </td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">new_name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>  <span class="pl-c"><span class="pl-c">#</span> Used for renaming the file</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">rename</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> file_name</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> file_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">		open_file()</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">	arr <span class="pl-k">=</span> file_name.split(<span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">	path <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">0</span> , <span class="pl-c1">len</span>(arr) <span class="pl-k">-</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">		path <span class="pl-k">=</span> path <span class="pl-k">+</span> arr[i] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">	new_name <span class="pl-k">=</span> simpledialog.askstring(<span class="pl-s"><span class="pl-pds">&quot;</span>Rename<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Enter new name<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">	os.rename(file_name , <span class="pl-c1">str</span>(path) <span class="pl-k">+</span> <span class="pl-c1">str</span>(new_name))</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">	file_name <span class="pl-k">=</span> <span class="pl-c1">str</span>(path) <span class="pl-k">+</span> <span class="pl-c1">str</span>(new_name)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">	master.title(file_name <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - Script Editor<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">close</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">	save()</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">	master.quit()</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> EDIT MENU METHODS</span></td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">cut</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span> first clear the previous text on the clipboard.</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">	master.clipboard_clear()</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">	text.clipboard_append(<span class="pl-v">string</span><span class="pl-k">=</span>text.selection_get())</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span>index of the first and yhe last letter of our selection.</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">	text.delete(<span class="pl-v">index1</span><span class="pl-k">=</span><span class="pl-c1">SEL_FIRST</span>, <span class="pl-v">index2</span><span class="pl-k">=</span><span class="pl-c1">SEL_LAST</span>)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">copy</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span> first clear the previous text on the clipboard.</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> text.index(<span class="pl-c1">SEL_FIRST</span>)</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> text.index(<span class="pl-c1">SEL_LAST</span>)</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">	master.clipboard_clear()</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">	text.clipboard_append(<span class="pl-v">string</span><span class="pl-k">=</span>text.selection_get())</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">paste</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span> get gives everyting from the clipboard and paste it on the current cursor position</span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span> it does&#39;nt removes it from the clipboard.</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">	text.insert(<span class="pl-c1">INSERT</span>, master.clipboard_get())</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">delete</span>():</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">	text.delete(<span class="pl-v">index1</span><span class="pl-k">=</span><span class="pl-c1">SEL_FIRST</span>, <span class="pl-v">index2</span><span class="pl-k">=</span><span class="pl-c1">SEL_LAST</span>)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">undo</span>():</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">	text.edit_undo()</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">redo</span>():</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">	text.edit_redo()</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">select_all</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">	text.tag_add(<span class="pl-c1">SEL</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">delete_all</span>():</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">	text.delete(<span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> TOOLS MENU METHODS</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">change_color</span>():</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">	color <span class="pl-k">=</span> colorchooser.askcolor(<span class="pl-v">initialcolor</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>#ff0000<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">	color_name <span class="pl-k">=</span> color[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> fontColor</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">	fontColor <span class="pl-k">=</span> color_name</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>font_color_change<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> first char is bold, so unbold the range</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">            text.tag_delete(<span class="pl-s"><span class="pl-pds">&quot;</span>font_color_change<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span> , <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> first char is normal, so bold the whole selection</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">            text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>font_color_change<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span> , <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">    	make_tag()</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Adding Search Functionality</span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">check</span>(<span class="pl-smi">value</span>):</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">    text.tag_remove(<span class="pl-s"><span class="pl-pds">&#39;</span>found<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>1.0<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    text.tag_config(<span class="pl-s"><span class="pl-pds">&#39;</span>found<span class="pl-pds">&#39;</span></span>, <span class="pl-v">foreground</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>red<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">    list_of_words <span class="pl-k">=</span> value.split(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> word <span class="pl-k">in</span> list_of_words:</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        idx <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1.0<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> idx:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">            idx <span class="pl-k">=</span> text.search(word, idx, <span class="pl-v">nocase</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">stopindex</span><span class="pl-k">=</span><span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> idx:</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">                lastidx <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>+<span class="pl-c1">%d</span>c<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (idx, <span class="pl-c1">len</span>(word))</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">                text.tag_add(<span class="pl-s"><span class="pl-pds">&#39;</span>found<span class="pl-pds">&#39;</span></span>, idx, lastidx)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> lastidx</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">                idx <span class="pl-k">=</span> lastidx</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> implementation of search dialog box - calling the check method to search and find_text_cancel_button to close it</span></td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">find_text</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">	search_toplevel <span class="pl-k">=</span> Toplevel(master)</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">	search_toplevel.title(<span class="pl-s"><span class="pl-pds">&#39;</span>Find Text<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">	search_toplevel.transient(master)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">	search_toplevel.resizable(<span class="pl-c1">False</span>, <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">	Label(search_toplevel, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Find All:<span class="pl-pds">&quot;</span></span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>e<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">	search_entry_widget <span class="pl-k">=</span> Entry(search_toplevel, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">25</span>)</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">	search_entry_widget.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>we<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">	search_entry_widget.focus_set()</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">	Button(search_toplevel, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Ok<span class="pl-pds">&quot;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: check( search_entry_widget.get())).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>e<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">5</span>)</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">	Button(search_toplevel, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Cancel<span class="pl-pds">&quot;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: find_text_cancel_button(search_toplevel)).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>e<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> remove search tags and destroys the search box</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">find_text_cancel_button</span>(<span class="pl-smi">search_toplevel</span>):</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">	text.tag_remove(<span class="pl-s"><span class="pl-pds">&#39;</span>found<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>1.0<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">	search_toplevel.destroy()</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&quot;</span>break<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> FORMAT BAR METHODS</span></td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">bold</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> first char is bold, so unbold the range</span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">            text.tag_delete(<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>,  <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> first char is normal, so bold the whole selection</span></td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">            text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">   	make_tag()</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">italic</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>italic<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">		text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>roman<span class="pl-pds">&quot;</span></span>,  <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">		text.tag_delete(<span class="pl-s"><span class="pl-pds">&quot;</span>italic<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">		text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>italic<span class="pl-pds">&quot;</span></span>,  <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">	make_tag()</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">underline</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>underline<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">            text.tag_delete(<span class="pl-s"><span class="pl-pds">&quot;</span>underline<span class="pl-pds">&quot;</span></span>,  <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">            text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>underline<span class="pl-pds">&quot;</span></span>,  <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        make_tag()</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">strike</span>():</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>overstrike<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">		text.tag_delete(<span class="pl-s"><span class="pl-pds">&quot;</span>overstrike<span class="pl-pds">&quot;</span></span> ,<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">		text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>overstrike<span class="pl-pds">&quot;</span></span> , <span class="pl-c1">1.0</span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">	make_tag()</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">highlight</span>():</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">	color <span class="pl-k">=</span> colorchooser.askcolor(<span class="pl-v">initialcolor</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>white<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">	color_rgb <span class="pl-k">=</span> color[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> fontBackground</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">   	fontBackground<span class="pl-k">=</span> color_rgb</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">	current_tags <span class="pl-k">=</span> text.tag_names()</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>background_color_change<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> current_tags:</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">            text.tag_delete(<span class="pl-s"><span class="pl-pds">&quot;</span>background_color_change<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">            text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>background_color_change<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">    	make_tag()</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> To make align functions work properly</span></td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">remove_align_tags</span>():</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">	all_tags <span class="pl-k">=</span> text.tag_names(<span class="pl-v">index</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>center<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> all_tags:</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">		text.tag_remove(<span class="pl-s"><span class="pl-pds">&quot;</span>center<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> all_tags:</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">		text.tag_remove(<span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>right<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> all_tags:</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">		text.tag_remove(<span class="pl-s"><span class="pl-pds">&quot;</span>right<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_center</span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">align_center</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">	remove_align_tags()</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">	text.tag_configure(<span class="pl-s"><span class="pl-pds">&quot;</span>center<span class="pl-pds">&quot;</span></span>, <span class="pl-v">justify</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>center<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">	text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>center<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>end<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_justify</span></td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">align_justify</span>():</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">	remove_align_tags()</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_left</span></td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">align_left</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">	remove_align_tags()</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">	text.tag_configure(<span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">justify</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">	text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>end<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_right</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">align_right</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">	remove_align_tags()</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">	text.tag_configure(<span class="pl-s"><span class="pl-pds">&quot;</span>right<span class="pl-pds">&quot;</span></span>, <span class="pl-v">justify</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>right<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">	text.tag_add(<span class="pl-s"><span class="pl-pds">&quot;</span>right<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1.0</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>end<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Font and size change functions - BINDED WITH THE COMBOBOX SELECTION</span></td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> change font and size are methods binded with combobox, calling fontit and sizeit</span></td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> called when &lt;&lt;combobox&gt;&gt; event is called</span></td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">change_font</span>(<span class="pl-smi">event</span>):</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">	f <span class="pl-k">=</span> all_fonts.get()</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> current_font_family</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">	current_font_family <span class="pl-k">=</span> f</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">	make_tag()</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">change_size</span>(<span class="pl-smi">event</span>):</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">	sz <span class="pl-k">=</span> <span class="pl-c1">int</span>(all_size.get())</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">global</span> current_font_size</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">	current_font_size <span class="pl-k">=</span> sz</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">	make_tag()</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> ------------- CREATING - MENUBAR AND ITS MENUS, TOOLS BAR, FORMAT BAR, STATUS BAR AND TEXT AREA -----------#</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">  </td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> TOOLBAR</span></td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">toolbar <span class="pl-k">=</span> Frame(master, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> TOOLBAR BUTTONS</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> new</span></td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">new_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b2<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>new, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">photo_new <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/new.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">photo_new <span class="pl-k">=</span> photo_new.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">image_new <span class="pl-k">=</span> ImageTk.PhotoImage(photo_new)</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">new_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_new)</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">new_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> save</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">save_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b1<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>save, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">photo_save <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/save.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">photo_save <span class="pl-k">=</span> photo_save.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">image_save <span class="pl-k">=</span> ImageTk.PhotoImage(photo_save)</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">save_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_save)</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">save_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>open</span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">open_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b3<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>open_file, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">photo_open <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/open.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">photo_open <span class="pl-k">=</span> photo_open.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">image_open <span class="pl-k">=</span> ImageTk.PhotoImage(photo_open)</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">open_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_open)</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">open_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> copy</span></td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">copy_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b4<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>copy, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">photo_copy <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/copy.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">photo_copy <span class="pl-k">=</span> photo_copy.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">image_copy <span class="pl-k">=</span> ImageTk.PhotoImage(photo_copy)</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">copy_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_copy)</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">copy_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>cut</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">cut_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b5<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>cut, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">photo_cut <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/cut.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">photo_cut <span class="pl-k">=</span> photo_cut.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">image_cut <span class="pl-k">=</span> ImageTk.PhotoImage(photo_cut)</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">cut_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_cut)</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">cut_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> paste</span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">paste_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b6<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>paste, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">photo_paste <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/paste.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">photo_paste <span class="pl-k">=</span> photo_paste.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">image_paste <span class="pl-k">=</span> ImageTk.PhotoImage(photo_paste)</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">paste_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_paste)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">paste_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> redo</span></td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">redo_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b7<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>redo, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">photo_redo <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/redo.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">photo_redo <span class="pl-k">=</span> photo_redo.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">image_redo <span class="pl-k">=</span> ImageTk.PhotoImage(photo_redo)</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">redo_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_redo)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">redo_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> undo</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">undo_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b8<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>undo, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">photo_undo <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/undo.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">photo_undo <span class="pl-k">=</span> photo_undo.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">image_undo <span class="pl-k">=</span> ImageTk.PhotoImage(photo_undo)</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">undo_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_undo)</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">undo_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> find</span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">find_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>toolbar_b9<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>find_text, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">photo_find <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/find.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">photo_find <span class="pl-k">=</span> photo_find.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">image_find <span class="pl-k">=</span> ImageTk.PhotoImage(photo_find)</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">find_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_find)</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">find_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>toolbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> FORMATTING BAR</span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">formattingbar <span class="pl-k">=</span> Frame(master, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> FORMATTING BAR COMBOBOX - FOR FONT AND SIZE</span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> font combobox</span></td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">all_fonts <span class="pl-k">=</span> StringVar()</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">font_menu <span class="pl-k">=</span> ttk.Combobox(formattingbar, <span class="pl-v">textvariable</span><span class="pl-k">=</span>all_fonts , <span class="pl-v">state</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>readonly<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">font_menu.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">font_menu[<span class="pl-s"><span class="pl-pds">&#39;</span>values<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> ( <span class="pl-s"><span class="pl-pds">&#39;</span>Courier<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Helvetica<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Liberation Mono<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>OpenSymbol<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Century Schoolbook L<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>DejaVu Sans Mono<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Ubuntu Condensed<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Ubuntu Mono<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Lohit Punjabi<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Mukti Narrow<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Meera<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Symbola<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Abyssinica SIL<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">font_menu.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;&lt;ComboboxSelected&gt;&gt;<span class="pl-pds">&#39;</span></span>,change_font)</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">font_menu.current(<span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> size combobox</span></td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">all_size <span class="pl-k">=</span> StringVar()</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">size_menu <span class="pl-k">=</span> ttk.Combobox(formattingbar, <span class="pl-v">textvariable</span><span class="pl-k">=</span>all_size , <span class="pl-v">state</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>readonly<span class="pl-pds">&#39;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">5</span>)</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">size_menu.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">size_menu[<span class="pl-s"><span class="pl-pds">&#39;</span>values<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>10<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>12<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>14<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>16<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>18<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>20<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>22<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>24<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>26<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>28<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>30<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">size_menu.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;&lt;ComboboxSelected&gt;&gt;<span class="pl-pds">&#39;</span></span>,change_size)</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">size_menu.current(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> FORMATBAR BUTTONS</span></td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>bold</span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">bold_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b1<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>bold, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">photo_bold <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/bold.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">photo_bold <span class="pl-k">=</span> photo_bold.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">image_bold <span class="pl-k">=</span> ImageTk.PhotoImage(photo_bold)</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">bold_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_bold)</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">bold_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> italic</span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">italic_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b2<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>italic, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">photo_italic <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/italic.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">photo_italic <span class="pl-k">=</span> photo_italic.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">image_italic <span class="pl-k">=</span> ImageTk.PhotoImage(photo_italic)</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">italic_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_italic)</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">italic_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> underline</span></td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">underline_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b3<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>underline, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">photo_underline <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/underline.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">photo_underline <span class="pl-k">=</span> photo_underline.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">image_underline <span class="pl-k">=</span> ImageTk.PhotoImage(photo_underline)</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">underline_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_underline)</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">underline_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> strike</span></td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">strike_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b4<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>strike, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">photo_strike <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/strike.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">photo_strike <span class="pl-k">=</span> photo_strike.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">image_strike <span class="pl-k">=</span> ImageTk.PhotoImage(photo_strike)</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">strike_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_strike)</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">strike_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> font_color</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">font_color_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b5<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>change_color, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">photo_font_color <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/font-color.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">photo_font_color <span class="pl-k">=</span> photo_font_color.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">image_font_color <span class="pl-k">=</span> ImageTk.PhotoImage(photo_font_color)</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">font_color_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_font_color)</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">font_color_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> highlight</span></td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">highlight_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b6<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>highlight, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">photo_highlight <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/highlight.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">photo_highlight <span class="pl-k">=</span> photo_highlight.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">image_highlight <span class="pl-k">=</span> ImageTk.PhotoImage(photo_highlight)</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">highlight_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_highlight)</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">highlight_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_center</span></td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">align_center_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b7<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>align_center, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">photo_align_center <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/align-center.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">photo_align_center <span class="pl-k">=</span> photo_align_center.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">image_align_center <span class="pl-k">=</span> ImageTk.PhotoImage(photo_align_center)</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">align_center_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_align_center)</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">align_center_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_justify</span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">align_justify_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b8<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>align_justify, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">photo_align_justify <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/align-justify.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">photo_align_justify <span class="pl-k">=</span> photo_align_justify.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">image_align_justify <span class="pl-k">=</span> ImageTk.PhotoImage(photo_align_justify)</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">align_justify_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_align_justify)</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">align_justify_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_left</span></td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">align_left_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b9<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>align_left, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">photo_align_left <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/align-left.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">photo_align_left <span class="pl-k">=</span> photo_align_left.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">image_align_left <span class="pl-k">=</span> ImageTk.PhotoImage(photo_align_left)</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">align_left_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_align_left)</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">align_left_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> align_right</span></td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">align_right_button <span class="pl-k">=</span> Button(<span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>formatbar_b10<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">command</span><span class="pl-k">=</span>align_right, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">photo_align_right <span class="pl-k">=</span> Image.open(<span class="pl-s"><span class="pl-pds">&quot;</span>icons/align-right.png<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">photo_align_right <span class="pl-k">=</span> photo_align_right.resize((<span class="pl-c1">18</span>, <span class="pl-c1">18</span>), Image.<span class="pl-c1">ANTIALIAS</span>)</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">image_align_right <span class="pl-k">=</span> ImageTk.PhotoImage(photo_align_right)</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">align_right_button.config(<span class="pl-v">image</span><span class="pl-k">=</span>image_align_right)</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">align_right_button.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>formattingbar, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> STATUS BAR</span></td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">status <span class="pl-k">=</span> Label(master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>, <span class="pl-v">bd</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">relief</span><span class="pl-k">=</span><span class="pl-c1">SUNKEN</span>, <span class="pl-v">anchor</span><span class="pl-k">=</span>W)</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> CREATING TEXT AREA - FIRST CREATED A FRAME AND THEN APPLIED TEXT OBJECT TO IT.</span></td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">text_frame <span class="pl-k">=</span> Frame(master, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">relief</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>sunken<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">text <span class="pl-k">=</span> Text(<span class="pl-v">wrap</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>word<span class="pl-pds">&quot;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Liberation Mono<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">12</span>), <span class="pl-v">background</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>white<span class="pl-pds">&quot;</span></span>, <span class="pl-v">borderwidth</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">highlightthickness</span><span class="pl-k">=</span><span class="pl-c1">0</span> , <span class="pl-v">undo</span><span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">text.pack(<span class="pl-v">in_</span><span class="pl-k">=</span>text_frame, <span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>left<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fill</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>both<span class="pl-pds">&quot;</span></span>, <span class="pl-v">expand</span><span class="pl-k">=</span><span class="pl-c1">True</span>) <span class="pl-c"><span class="pl-c">#</span> pack text object.</span></td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> PACK TOOLBAR, FORMATBAR, STATUSBAR AND TEXT FRAME.</span></td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">toolbar.pack(<span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>top<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fill</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>x<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">formattingbar.pack(<span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>top<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fill</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>x<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">status.pack(<span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>bottom<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fill</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>x<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">text_frame.pack(<span class="pl-v">side</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>bottom<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fill</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>both<span class="pl-pds">&quot;</span></span>, <span class="pl-v">expand</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">text.focus_set()</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> MENUBAR CREATION</span></td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">menu <span class="pl-k">=</span> Menu(master)</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">master.config(<span class="pl-v">menu</span><span class="pl-k">=</span>menu)</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> File menu.</span></td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">file_menu <span class="pl-k">=</span> Menu(menu)</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">menu.add_cascade(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>File<span class="pl-pds">&quot;</span></span>, <span class="pl-v">menu</span><span class="pl-k">=</span>file_menu, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">file_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>New<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>new, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_new, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+N<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>) <span class="pl-c"><span class="pl-c">#</span> command passed is here the method defined above.</span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">file_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Open<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>open_file, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_open, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+O<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">file_menu.add_separator()</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">file_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Save<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>save, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_save, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+S<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">file_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Save As<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>save_as, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+Shift+S<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">file_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Rename<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>rename, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+Shift+R<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">file_menu.add_separator()</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">file_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Close<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>close, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Alt+F4<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Edit Menu.</span></td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">edit_menu <span class="pl-k">=</span> Menu(menu)</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">menu.add_cascade(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Edit<span class="pl-pds">&quot;</span></span>, <span class="pl-v">menu</span><span class="pl-k">=</span>edit_menu, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Undo<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>undo, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_undo, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+Z<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Redo<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>redo, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_redo, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+Y<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">edit_menu.add_separator()</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Cut<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>cut, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_cut, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+X<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Copy<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>copy, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_copy, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+C<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Paste<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>paste, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_paste, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+P<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Delete<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>delete, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">edit_menu.add_separator()</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Select All<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>select_all, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+A<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">edit_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Clear All<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>delete_all, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">6</span>)</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Tool Menu</span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">tool_menu <span class="pl-k">=</span> Menu(menu)</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">menu.add_cascade(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Tools<span class="pl-pds">&quot;</span></span>, <span class="pl-v">menu</span><span class="pl-k">=</span>tool_menu, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">tool_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Change Color<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>change_color)</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">tool_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Search<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>find_text, <span class="pl-v">compound</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">image</span><span class="pl-k">=</span>image_find, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+F<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Help Menu</span></td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">about</span>(<span class="pl-smi">event</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">	messagebox.showinfo(<span class="pl-s"><span class="pl-pds">&quot;</span>About<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Text Editor<span class="pl-cce">\n</span>Created in Python using Tkinter<span class="pl-cce">\n</span>Copyright with Amandeep and Harmanpreet, 2017<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">help_menu <span class="pl-k">=</span> Menu(menu)</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">menu.add_cascade(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Help<span class="pl-pds">&quot;</span></span>, <span class="pl-v">menu</span><span class="pl-k">=</span>help_menu, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">help_menu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>About<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>about, <span class="pl-v">accelerator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Ctrl+H<span class="pl-pds">&#39;</span></span>, <span class="pl-v">underline</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> ----- BINDING ALL KEYBOARD SHORTCUTS ---------- #</span></td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-n&gt;<span class="pl-pds">&#39;</span></span>, new)</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-N&gt;<span class="pl-pds">&#39;</span></span>, new) </td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-o&gt;<span class="pl-pds">&#39;</span></span>, open_file)</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-O&gt;<span class="pl-pds">&#39;</span></span>, open_file)</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-s&gt;<span class="pl-pds">&#39;</span></span>, save)</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-S&gt;<span class="pl-pds">&#39;</span></span>, save)</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-s&gt;<span class="pl-pds">&#39;</span></span>, save_as)</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-S&gt;<span class="pl-pds">&#39;</span></span>, save_as)</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-r&gt;<span class="pl-pds">&#39;</span></span>, rename)</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-R&gt;<span class="pl-pds">&#39;</span></span>, rename)</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Alt-F4&gt;<span class="pl-pds">&#39;</span></span>, close)</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Alt-F4&gt;<span class="pl-pds">&#39;</span></span>, close)</td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-x&gt;<span class="pl-pds">&#39;</span></span>, cut)</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-X&gt;<span class="pl-pds">&#39;</span></span>, cut)</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-c&gt;<span class="pl-pds">&#39;</span></span>, copy)</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-C&gt;<span class="pl-pds">&#39;</span></span>, copy)</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-p&gt;<span class="pl-pds">&#39;</span></span>, paste)</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-P&gt;<span class="pl-pds">&#39;</span></span>, paste)</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-a&gt;<span class="pl-pds">&#39;</span></span>, select_all)</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-A&gt;<span class="pl-pds">&#39;</span></span>, select_all)</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-h&gt;<span class="pl-pds">&#39;</span></span>, about)</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-H&gt;<span class="pl-pds">&#39;</span></span>, about)</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-f&gt;<span class="pl-pds">&#39;</span></span>, find_text)</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-F&gt;<span class="pl-pds">&#39;</span></span>, find_text)</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-i&gt;<span class="pl-pds">&#39;</span></span>, italic)</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-I&gt;<span class="pl-pds">&#39;</span></span>, italic)</td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-b&gt;<span class="pl-pds">&#39;</span></span>, bold)</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-B&gt;<span class="pl-pds">&#39;</span></span>, bold)</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-u&gt;<span class="pl-pds">&#39;</span></span>, underline)</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-U&gt;<span class="pl-pds">&#39;</span></span>, underline)</td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-l&gt;<span class="pl-pds">&#39;</span></span>, align_left)</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-L&gt;<span class="pl-pds">&#39;</span></span>, align_left)</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-r&gt;<span class="pl-pds">&#39;</span></span>, align_right)</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-R&gt;<span class="pl-pds">&#39;</span></span>, align_right)</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-c&gt;<span class="pl-pds">&#39;</span></span>, align_center)</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">text.bind(<span class="pl-s"><span class="pl-pds">&#39;</span>&lt;Control-Shift-C&gt;<span class="pl-pds">&#39;</span></span>, align_center)</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> ---------- SETTING EVENTS FOR THE STATUS BAR -------------- #</span></td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">on_enter</span>(<span class="pl-smi">event</span>, <span class="pl-smi">str</span>):</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">	status.configure(<span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-c1">str</span>)</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">on_leave</span>(<span class="pl-smi">event</span>):</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">	status.configure(<span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">new_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>New, Command - Ctrl+N<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">new_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">save_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Save, Command - Ctrl+S<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">save_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">open_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Open, Command - Ctrl+O<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">open_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">copy_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Copy, Command - Ctrl+C<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">copy_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">cut_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Cut, Command - Ctrl+X<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">cut_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">paste_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Paste, Command - Ctrl+P<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">paste_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">undo_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Undo, Command - Ctrl+Z<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">undo_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">redo_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Redo, Command - Ctrl+Y<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">redo_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">find_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Find, Command - Ctrl+F<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">find_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">bold_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Bold, Command - Ctrl+B<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">bold_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">italic_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Italic, Command - Ctrl+Shift+I<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">italic_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">underline_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Underline, Command - Ctrl+U<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">underline_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">align_justify_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Justify<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">align_justify_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">align_left_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Align Left, Command - Control-Shift-L<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">align_left_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">align_right_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Align Right, Command - Control-Shift-R<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">align_right_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">align_center_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Align Center, Command - Control-Shift-C<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">align_center_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">strike_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Strike<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">strike_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">font_color_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Font Color<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">font_color_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">highlight_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Highlight<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">highlight_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">strike_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Enter&gt;<span class="pl-pds">&quot;</span></span>, <span class="pl-k">lambda</span> <span class="pl-smi">event</span> , <span class="pl-smi">str</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Strike<span class="pl-pds">&quot;</span></span>:on_enter(event , <span class="pl-c1">str</span>))</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">strike_button.bind(<span class="pl-s"><span class="pl-pds">&quot;</span>&lt;Leave&gt;<span class="pl-pds">&quot;</span></span>, on_leave)</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> MAINLOOP OF THE PROGRAM</span></td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">master.mainloop()</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/amandeep511997/Text-Editor/blame/8ef6bc2aa5c315d798630e6cd8835087284756c6/main.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/amandeep511997/Text-Editor/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/amandeep511997/Text-Editor/find-symbols"
     data-tagsearch-ref="master"
     data-tagsearch-path="main.py"
     data-tagsearch-lang="Python"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:116910473,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;client_id&quot;:&quot;1916191685.1568368095&quot;,&quot;originating_request_id&quot;:&quot;8398:290C:9D365D:EB7997:5E0BC10F&quot;,&quot;originating_url&quot;:&quot;https://github.com/amandeep511997/Text-Editor/blob/master/main.py&quot;,&quot;referrer&quot;:&quot;https://github.com/amandeep511997/Text-Editor/find/master&quot;,&quot;user_id&quot;:55187704}}"
     data-hydro-click-hmac="2478a5a2275fa3f88cd2a408914dd66ae11ff820ea7017146b9bd5c1a961d97b">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2019 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-mdrBasYG+QjgS391PSyVkPr06io3gWplCVbPscguetNEHxIEt+mZwCeCxPR9eMNfda6qNuibNFqBo5ak2+O/hg==" type="application/javascript" src="https://github.githubassets.com/assets/compat-bootstrap-99dac16a.js"></script>
    <script crossorigin="anonymous" integrity="sha512-/VSJJF96vCzSgC6y09Z4FqzjjuXRWOKIq2twF0Nb5/v8xy4qzngnH6Au6TFwbmNN/lborYJsojEpgIbYjoGvHQ==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-fd548924.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-0mcBYsTTDNy016WuG7Zu/Pb5dsdoVzVb5FlxH4btAPKKyTBKn+5g6N6lXxmMo1WokYH8uOYuLpTgLjU29jSqcA==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-d2670162.js"></script>
    
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

