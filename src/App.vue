<template>
  <div class="page-grid">
    <div>
      <div class="title">
        <!-- <img class="flag flag--left" src="./assets/CN.png"> -->
        <span>osu-wiki ZH status</span>
        <!-- <span class="title__last-update">last updated Wed, 21 Apr 2021 08:40:51 GMT</span> -->
      </div>

      <div class="section">
        <div class="section__title">
          Articles status compared (up-to-date in English)
        </div>

        <table>
          <tbody>
            <dl v-for="(dict, key) in json" v-bind:key="key">
              <dt class="Link--primary">
                <a :href="'https://github.com/ppy/osu-wiki/blob/master/'+dict.zh.path" target="_blank">
                  {{dict.zh.path}}
                </a>
              </dt>
              <ul>
                <li class="Link--primary">
                  <a :href="'https://github.com/ppy/osu-wiki/blob/master/'+dict.zh.path" target="_blank">
                  <img class="flag flag--left" src="./assets/CN.png">
                  zh.md
                  </a>
                </li>
                <span class="commit">
                  latest commit
                </span>
                <span class="commit commit_sha">
                  <a :href="'https://github.com/ppy/osu-wiki/commit/'+dict.zh.sha" target="_blank">
                    {{dict.zh.sha}}
                  </a>
                </span>
                <span class="title__last-update">
                  {{dict.zh.date}} UTC
                </span>
              </ul>
              <ul>
                <li class="Link--primary">
                  <a :href="'https://github.com/ppy/osu-wiki/blob/master/'+dict.en.path" target="_blank">
                  <img class="flag flag--left" src="./assets/GB.png">
                  en.md
                  </a>
                </li>
                <span class="commit">
                  latest commit 
                </span>
                <span class="commit commit_sha">
                  <a :href="'https://github.com/ppy/osu-wiki/commit/'+dict.en.sha" target="_blank">
                  {{dict.en.sha}}
                  </a>
                </span>
                <span class="title__last-update">
                  {{dict.en.date}} UTC
                </span>
              </ul>
            </dl>
          </tbody>
        </table>

      </div>
    </div>
  </div>
</template>
<style src="./css/style.css" scope></style>
<script>
import json from "./data/data.json";

export default {
  data() {
    return {
      json: json,
    };
  },
};
</script>
