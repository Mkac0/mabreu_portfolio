import { useContext } from 'react';
import { Link } from 'react-router';

const NavBar = () => {
    return (
        <nav className='site-header'>
            <Link to="/" className="portfolio">Melissa Abreu</Link>
            <ul className='nav-items'>
                <li><Link to="/about-me">About Me</Link></li>
                <li><Link to="/projects">Projects</Link></li>
                <li><Link to="/skills">Skills</Link></li>
                <li><Link to="/resume">Resume</Link></li>
            </ul>
        </nav>
    );
}

export default NavBar;