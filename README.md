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

2. Разметка дисков:

cfdisk /dev/nvme0n1 или /dev/{sdaX}
<ol>
  <li>efi раздел на 512mb или 1G</li>

  <li>root на 120GB и выше</li>

  <li>home на все остальное но можно и без него нужен для более удобного переноса данных</li>
</ol>

3. форматирование разделов: 
<ol>
  <li>mkfs.vfat/mkfs.fat -F 32 /dev/{раздел efi}</li>
  <li>mkfs.ext4/mkfs.btrfs/mkfs.xfs /dev/{разделы root и home если есть}</li>
</ol>

4. монтирование разделов и создание папок:
<ol>
  <li>mount /dev/{раздел root} /mnt</li>
  <li>mkdir -p /mnt/boot/efi</li>
  <li>mount /dev/{раздел efi} /mnt/boot/efi</li>
</ol>
