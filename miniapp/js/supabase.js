const SUPABASE_URL = 'https://tiifrhxyosmkfizpfcuz.supabase.co';
const SUPABASE_KEY = 'sb_publishable_DDwOXAwmhAHhiUHGLhWzXA_zt4tv7X5';

const supabase = {

  async getActiveCoins(telegramUserId) {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/user_coins?telegram_user_id=eq.${telegramUserId}&is_active=eq.true&select=coin_symbol`,
      { headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}` } }
    );
    const data = await res.json();
    return data.map(row => row.coin_symbol);
  },

  async setCoinActive(telegramUserId, coinSymbol, isActive) {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/user_coins?telegram_user_id=eq.${telegramUserId}&coin_symbol=eq.${coinSymbol}`,
      {
        method: 'PATCH',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=representation'
        },
        body: JSON.stringify({ is_active: isActive })
      }
    );
    const data = await res.json();
    if (Array.isArray(data) && data.length === 0) {
      const res2 = await fetch(`${SUPABASE_URL}/rest/v1/user_coins`, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ telegram_user_id: telegramUserId, coin_symbol: coinSymbol, is_active: isActive })
      });
      return res2.ok;
    }
    return res.ok;
  },

  async resetToDefaults(telegramUserId) {
    const defaults = ['BTC','ETH','USDT','XRP','SOL'];
    const allCoins = [
      'BTC','ETH','USDT','XRP','SOL','USDC','TRX','HYPE','ADA','DOGE',
      'AVAX','SUI','LINK','DOT','LTC','POL','SHIB','BCH','TON','UNI',
      'ICP','NEAR','APT','XLM','ATOM','FIL','ARB','OP','XMR','PEPE'
    ];
    await Promise.all(allCoins.map(symbol =>
      fetch(
        `${SUPABASE_URL}/rest/v1/user_coins?telegram_user_id=eq.${telegramUserId}&coin_symbol=eq.${symbol}`,
        {
          method: 'PATCH',
          headers: {
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ is_active: defaults.includes(symbol) })
        }
      )
    ));
    return true;
  }
};