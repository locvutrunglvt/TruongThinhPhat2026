// api/data.js - Vercel Serverless Function
export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  return res.status(200).json({
    project: 'FSC Văn Hán - Trường Thịnh Phát 2026',
    certificateCode: 'FSC-C183027',
    status: 'online',
    platform: 'Vercel Edge / Serverless Network',
    updatedAt: new Date().toISOString()
  });
}

