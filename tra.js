import { pipeline } from '@xenova/transformers';
async function aio (){
const pipe = await pipeline('translation', 'Xenova/opus-mt-mul-en');

}
aio();