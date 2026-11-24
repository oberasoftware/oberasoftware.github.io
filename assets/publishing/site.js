// Optional progressive enhancement. Navigation and support work without JS.
const galleryButtons=[...document.querySelectorAll('[data-gallery-image]')];
if(galleryButtons.length){
 const dialog=document.querySelector('#media-viewer');let index=0,opener;
 const picture=dialog.querySelector('img'),caption=dialog.querySelector('[data-caption]');
 function show(next){index=(next+galleryButtons.length)%galleryButtons.length;const item=galleryButtons[index];picture.src=item.dataset.galleryImage;picture.alt=item.dataset.caption;caption.textContent=item.dataset.caption;}
 galleryButtons.forEach((button,i)=>button.addEventListener('click',event=>{event.preventDefault();opener=button;show(i);dialog.showModal();}));
 dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());
 dialog.querySelector('[data-prev]').addEventListener('click',()=>show(index-1));
 dialog.querySelector('[data-next]').addEventListener('click',()=>show(index+1));
 dialog.addEventListener('close',()=>opener?.focus());
 dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
 dialog.addEventListener('keydown',event=>{if(event.key==='ArrowLeft'){event.preventDefault();show(index-1);}if(event.key==='ArrowRight'){event.preventDefault();show(index+1);}});
}
