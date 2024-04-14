<h1>
  Install Arch
</h1>

1. Загрузка в arch

подключение wifi:
<ol>
  <li>iwctl</li>

  <li>station {interface} scan</li>

  <li>station {interface} get-networks</li>

  <li>station {interface} connect {network}</li>

  <li>и проверить ping 1.1.1.1</li>
</ol>

2. Разметка дисков

cfdisk /dev/nvme0n1 или /dev/{sdaX}

efi раздел на 512mb или 1G

root на 120GB и выше

home на все остальное но можно и без него нужен для более удобного переноса данных

3. форматирование разделов
mkfs.vfat/mkfs.fat -F 32 /dev/{раздел efi}
mkfs.ext4/mkfs.btrfs/mkfs.xfs /dev/{разделы root и home если есть}

4. монтирование разделов и создание папок
mount /dev/{раздел root} /mnt
mkdir -p /mnt/boot/efi
mount /dev/{раздел efi} /mnt/boot/efi


4. pac
