import { app as e, BrowserWindow as t } from "electron";
import i from "path";
import { fileURLToPath as r } from "url";
const a = r(import.meta.url), l = i.dirname(a);
function o() {
  const n = new t({
    width: 1800,
    height: 1e3,
    title: "All In One Swiper",
    autoHideMenuBar: !0,
    webPreferences: {
      nodeIntegration: !0,
      contextIsolation: !1
    }
  });
  process.env.VITE_DEV_SERVER_URL ? n.loadURL(process.env.VITE_DEV_SERVER_URL) : n.loadFile(i.join(l, "../dist/index.html"));
}
e.whenReady().then(() => {
  o(), e.on("activate", () => {
    t.getAllWindows().length === 0 && o();
  });
});
e.on("window-all-closed", () => {
  process.platform !== "darwin" && e.quit();
});
