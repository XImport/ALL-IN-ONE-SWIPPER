import { app, BrowserWindow } from 'electron';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
function createWindow() {
    const win = new BrowserWindow({
      width: 1800,
      height: 1000,
      title : "All In One Swiper",
      autoHideMenuBar : false,
      webPreferences: {
        nodeIntegration: true,
        contextIsolation: false
  
      }
    })
  
    // In development, load the local dev server
    if (process.env.VITE_DEV_SERVER_URL) {
      win.loadURL(process.env.VITE_DEV_SERVER_URL)
      // win.webContents.openDevTools()
    } else {
      // In production, load the built files
      win.loadFile(path.join(__dirname, '../dist/index.html'))
    }
  }
  
  app.whenReady().then(() => {
    createWindow()
  
    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
      }
    })
  })
  
  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })