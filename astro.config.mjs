// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://y999gameapp.com.pk",
  vite: {
    plugins: [tailwindcss()],
  },
  integrations: [
    sitemap({
      changefreq: "weekly",
      priority: 0.7,
      filter: (page) =>
        !page.includes("/disclaimer") &&
        !page.includes("/privacy-policy") &&
        !page.includes("/terms-conditions"),
    }),
  ],
});
