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
<ol>
  <li>fdisk -l</li>
  <li>cfdisk /dev/nvme0n1 или /dev/{sdaX}</li>
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

5. Установка базовой системы и вход в chroot
<ol>
  <li>pacstrap -i /mnt base linux linux-firmware sof-firmware amd-ucode iwd neovim</li>
  <li>genfstab -U /mnt >> /mnt/etc/fstab</li>
  <li>arch-chroot /mnt</li>
</ol>

6. базовая астройка системы
<ol>
  <li>ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime</li>
  <li>hwclock --systohc</li>
  <li>редактирование /etc/locale.gen</li>
  <li>echo "ru_RU.UTF-8" > /etc/locale.conf</li>
  <li>echo "FONT=cyr-sun16" > /etc/vconsole.conf</li>
  <li>echo "archlinux" > /etc/hostname</li>
  <li>pacman -S grub os-prober efibootmgr</li>
  <li>grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub --recheck</li>
  <li>passwd</li>
</ol>

7. Выход и перезагрузка:
<ol>
  <li>exit</li>
  <li>umount -R /mnt</li>
  <li>shutdown -r now</li>
</ol>
