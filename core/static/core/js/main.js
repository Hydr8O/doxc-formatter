const stopTransitionOnLoad = () => {
    document.body.classList.remove('stop-transition')
};


const addDropUploadHandlers = () => {
    const dropZone = document.querySelector('.drop-zone--out');
    const dropZoneIn = dropZone.querySelector('.drop-zone--in');
    const thumbnail = document.querySelector('.drop-zone__thumbnail');
    const dropInput = dropZone.querySelector('.drop-zone__input');
    const dropPlaceholder = dropZone.querySelector('.drop-zone__placeholder');
    
    dropZone.addEventListener('drop', e => {
        e.preventDefault();

        if (e.dataTransfer.files.length) {
            dropInput.files = e.dataTransfer.files;
            updateThumbnail(e.dataTransfer.files[0].name);
        }
    });

    dropZone.addEventListener('click', (e) => {
        dropInput.click();
    });

    dropZone.addEventListener('dragover', e => {
        e.preventDefault();
        dropZone.classList.add('drop-zone--over');
        dropZoneIn.classList.add('drop-zone--in--over');
    });

    ['dragend', 'dragleave'].forEach(type => {
        dropZone.addEventListener(type, () => {
            dropZone.classList.remove('drop-zone--over');
            dropZoneIn.classList.remove('drop-zone--in--over');
        });
    });

    dropInput.addEventListener('change', () => {
        if (dropInput.files.length) {
            updateThumbnail(dropInput.files[0].name);
        }
    });

    updateThumbnail = (docName) => {
        if (dropZone.querySelector('.drop-zone__placeholder')) {
            dropZone.querySelector('.drop-zone__placeholder').remove();
        }
        dropZone.classList.remove('drop-zone--over');
        dropZoneIn.classList.remove('drop-zone--in--over');
        thumbnail.classList.remove('hidden');
        thumbnail.dataset.label = docName; 
    };
};

stopTransitionOnLoad();
addDropUploadHandlers();